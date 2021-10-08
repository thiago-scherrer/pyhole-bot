import os
import re
import urllib.request


class UrlList:

    def __init__(self):
        self.tmpfile = '/tmp/pyhole_tmp_blocklist.txt'
        self.endpoint = None
        self.output = None

    def env_setup(self):
        try:
            self.endpoint = os.environ['URL_FILE']
        except KeyError:
            return "ENV URL_FILE required!"

        try:
            self.output = os.environ['BLOCKLIST_OUTPUT']
        except KeyError:
            return "ENV BLOCKLIST_OUTPUT required!"

    def get_endpoints(self):
        self.env_setup()

        try:
            result = []
            with open(self.endpoint) as f:
                lines = f.readlines()
                for self.endpoint in lines:
                    self.get_block_list(self.endpoint)
                    result.append(self.endpoint)
                return result

        except FileNotFoundError:
            return "Endpoint file not found!"

    def get_block_list(self, endpoint):
        try:
            with urllib.request.urlopen(endpoint) as f:
                result = f.read().decode('utf-8')
                normalized = self.url_normalizer(result)
                self.create_blocklist(normalized)
                return result

        except Exception:
            print(f"Failed trying to access endpoint: {endpoint}")
            pass

    def url_normalizer(self, blocklist):
        regex = re.compile(
                r'(?m)^#(.*)|'
                r'(?m)^repo(.*)|'
                r'(0.0.0.0)|'
                r'(127.0.0.1)|'
                r'(localhost)|'
                r'((?m)@)|'
                r'((?m)\:(.*))|'
                r'(<br>)|'
                r'(<BR>)|'
                r'(\s\s)|'
                r'( )|', re.IGNORECASE)
        return re.sub(regex, '', blocklist)

    def create_blocklist(self, blocklist):
        tmp = self.tmpfile
        fo = open(tmp, 'a')
        return fo.write(blocklist)

    def url_uniq(self):
        self.env_setup()

        lines_seen = set()

        if os.path.exists(self.output):
            os.remove(self.output)

        try:
            output_blocklist = open(self.output, 'x')
            for line in open(self.tmpfile, "r"):
                if line not in lines_seen:
                    output_blocklist.write(line)
                    lines_seen.add(line)
            output_blocklist.close()

        except KeyError:
            return "ENV BLOCKLIST_OUTPUT required!"

    def cleanup(self):
        if os.path.exists(self.tmpfile):
            os.remove(self.tmpfile)

        f = open(self.tmpfile, "x")
        return f.closed
