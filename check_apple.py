from concurrent.futures import ThreadPoolExecutor
from typing import Generator, Iterable
from functools import lru_cache
from time import sleep, ctime

from base import MacBook, MODEL_REFURB_URL, FIND_TERMS, BASE_URL, WAIT_SECONDS,\
    THREADS, LRU_CACHE_SIZE, SEND_EMAIL
from parse import HtmlWrapper
from send import send_macbook_msg

from requests import get


def wrap_page(url: str=MODEL_REFURB_URL) -> HtmlWrapper:
    response = get(url)

    return HtmlWrapper(response.content)


def gen_products(page: HtmlWrapper) -> Generator[HtmlWrapper, None, None]:
    products = page.find_all('tr', 'product', gen=True)  # lazy loader

    yield from products


@lru_cache(maxsize=LRU_CACHE_SIZE)
def get_specs(product: HtmlWrapper) -> str:
    return product.find('td', 'specs').text.strip()


def is_match(specs: str, terms: Iterable[str]=FIND_TERMS) -> bool:
    return all(term in specs for term in terms)


def gen_filter_products(products: Iterable[HtmlWrapper],
                        terms: Iterable[str]=FIND_TERMS) -> Generator[HtmlWrapper, None, None]:
    for product in products:
        specs = get_specs(product)

        if is_match(specs, terms):
            yield product


def get_macbook(product: HtmlWrapper) -> MacBook:
    header = product.h3.a

    title = header.text.strip()
    link = BASE_URL + header['href']
    price = product.find('span', 'price').text.strip()
    specs = get_specs(product)

    return MacBook(title, link, price, specs)


def gen_macbooks(products: Iterable[HtmlWrapper]) -> Generator[MacBook, None, None]:
    for product in products:
        yield get_macbook(product)


def gen_filter_macbooks(macbooks: Iterable[MacBook],
                        terms: Iterable[str]=FIND_TERMS) -> Generator[MacBook, None, None]:
    for macbook in macbooks:
        if is_match(macbook.specs, terms):
            yield macbook


def check_macbooks(page: HtmlWrapper,
                   terms: Iterable[str]=FIND_TERMS) -> Generator[MacBook, None, None]:
    products_gen = gen_products(page)
    filter_gen = gen_filter_products(products_gen, terms)
    macbooks_gen = gen_macbooks(filter_gen)

    yield from macbooks_gen


def consume_macbooks(page: HtmlWrapper,
                     terms: Iterable[str],
                     pool: ThreadPoolExecutor,
                     seen: set,
                     send_email: bool) -> None:

    for macbook in check_macbooks(page, terms):
        print(macbook, "\n")

        if macbook not in seen:
            if send_email:
                pool.submit(send_macbook_msg, macbook)

            seen.add(macbook)


def loop(url: str=MODEL_REFURB_URL,
         terms: Iterable[str]=FIND_TERMS,
         wait: float=WAIT_SECONDS,
         send_email: bool=SEND_EMAIL) -> None:

    seen = set()

    with ThreadPoolExecutor(THREADS) as pool:
        while True:
            page = wrap_page(url)
            consume_macbooks(page, terms, pool, seen, send_email)

            print("Seen:", len(seen), "@", ctime(), "Sleep:", wait)
            sleep(wait)


def main():
    loop()


if __name__ == "__main__":
    main()
