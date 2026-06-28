import re

class ContentTrimmer:
    """
    Keeps only product-relevant text before sending it to the LLM.
    """
    KEYWORDS = (
    "processor",
    "cpu",
    "gpu",
    "display",
    "screen",
    "ram",
    "memory",
    "storage",
    "ssd",
    "battery",
    "camera",
    "chip",
    "chipset",
    "weight",
    "dimensions",
    "wireless",
    "wifi",
    "bluetooth",
    "ports",
    "usb",
    "thunderbolt",
    "speaker",
    "keyboard",
    "touchpad",
    "price",
    )
    IGNORE_LINES = (
    "privacy policy",
    "shipping",
    "returns",
    "accessories",
    "buy now",
    "sign in",
    "cart",
    "wishlist",
    "support",
    "home",
    )
    MIN_BLOCK_SCORE = 2
    SPEC_PATTERN = re.compile(
    r"\d+\s?(GB|TB|MB|MHz|GHz|mAh|Wh|inch|\"|nm|MP|Hz|W)",
    re.IGNORECASE,)
    PRODUCT_PATTERN = re.compile(
    r"[A-Za-z]+.*\d+"
)

    def trim(self, text: str) -> str:
        """
        Keep only relevant content blocks.
        """

        blocks = self._split_into_blocks(text)

        kept_blocks = []

        for block in blocks:
            if self._is_relevant_block(block):
                kept_blocks.append(block)

        return "\n\n".join(kept_blocks)
        
    def _split_into_blocks(self, text: str) -> list[str]:
        """
        Split text into logical blocks separated by blank lines.
        """

        blocks = []

        current_block = []

        for line in text.splitlines():

            line = line.strip()

            if line:

                current_block.append(line)

            elif current_block:

                blocks.append("\n".join(current_block))
                current_block = []

        if current_block:
            blocks.append("\n".join(current_block))

        return blocks
    
    def _score_block(self, block: str) -> int:
        """
        Assign a relevance score to a block of text.
        """

        score = 0

        block_lower = block.lower()

        # Ignore blocks containing unwanted content
        if any(ignore in block_lower for ignore in self.IGNORE_LINES):
            return -100

        # Product name
        if self.PRODUCT_PATTERN.search(block):
            score += 2

        # Specification values
        if self.SPEC_PATTERN.search(block):
            score += 2

        # Keywords
        for keyword in self.KEYWORDS:
            if keyword in block_lower:
                score += 1

        return score
    def _is_relevant_block(self, block: str) -> bool:
        """
        Determine whether a block should be kept.
        """

        return self._score_block(block) >= self.MIN_BLOCK_SCORE