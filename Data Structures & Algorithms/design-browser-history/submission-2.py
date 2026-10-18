class page:
    
    def __init__(self, url="", prev=None, next=None):
        self.url, self.prev, self.next = url, prev, next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = page(homepage)
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        nxt = page(url, self.cur)
        self.cur.next = nxt
        self.cur = nxt

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.prev == None:
                return self.homepage.url
            self.cur = self.cur.prev
        return self.cur.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.next == None:
                return self.cur.url
            self.cur = self.cur.next
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)