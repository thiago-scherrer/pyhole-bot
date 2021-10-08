#!/usr/bin/env python3
import get_list


def main():
    pyhole = get_list.UrlList()
    print(pyhole.env_setup())
    pyhole.cleanup()
    pyhole.get_endpoints()
    pyhole.url_uniq()


if __name__ == "__main__":
    main()
