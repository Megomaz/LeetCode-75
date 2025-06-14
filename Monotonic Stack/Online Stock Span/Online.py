class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  # Start with a span of 1 for today

        # While stack is not empty and top price <= current price
        while self.stack and self.stack[-1][0] <= price:
            # Add their span to ours, since they’re part of the span
            span += self.stack.pop()[1]

        # Push the current price and its span onto the stack
        self.stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)