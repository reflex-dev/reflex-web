import black

from flexdown import types
from flexdown.blocks.markdown_block import MarkdownBlock


class CodeBlock(MarkdownBlock):
    """A block of code."""

    starting_indicator = "```"
    ending_indicator = "```"
    include_indicators = True

    def get_content(self, env: types.Env) -> str:
        """The content of the block.

        Args:
            env: The environment variables to use for line transformations.

        Returns:
            The content of the block.
        """
        content = super().get_content(env)
        lines = content.splitlines()
        if "python" not in lines[0]:
            return content
        code_lines = "\n".join(lines[1:-1])
        try:
            formatted_code = black.format_str(
                code_lines, mode=black.FileMode(line_length=60)
            )
        except:
            formatted_code = code_lines
        content = "\n".join([lines[0], formatted_code.strip(), lines[-1]])
        return content
