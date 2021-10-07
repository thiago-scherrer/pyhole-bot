#!/usr/bin/env python
import os
import urllib.request


class UrlList:
    def get_endpoints(self):

        try:
            endpoints = os.environ['URL_FILE']
            result = []
            with open(endpoints) as f:
                lines = f.readlines()
                for endpoint in lines:
                    self.get_block_list(endpoint)
                    result.append(endpoint)
                return result

        except FileNotFoundError:
            return "Endpoint file not found!"

        except KeyError:
            return "Env URL_FILE required!"

    def get_block_list(self, endpoint):

        with urllib.request.urlopen(endpoint) as f:
            return(f.read().decode('utf-8'))
