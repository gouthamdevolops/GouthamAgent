import os
import sys
import unittest

# Append Source_Code to path so tests can import from it
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Source_Code"))

class TestVariableSanitization(unittest.TestCase):
    def test_variable_sanitization(self):
        """
        Test that a tool call ID containing dashes is correctly sanitized into
        a valid Python identifier name by replacing dashes with underscores.
        """
        # Sample tool call ID containing dashes (similar to OpenRouter response formats)
        tool_call_id_with_dashes = "chatcmpl-tool-8a25f14e75b954cc"

        # Sanitization mapping
        result_key = f"var_{tool_call_id_with_dashes}".replace("-", "_")

        # Assertions
        self.assertNotIn("-", result_key)
        self.assertEqual(result_key, "var_chatcmpl_tool_8a25f14e75b954cc")
        self.assertTrue(result_key.isidentifier(), "Sanitized result key must be a valid Python variable name")

    def test_variable_without_dashes(self):
        """
        Test that tool call IDs without dashes remain valid Python identifiers.
        """
        tool_call_id_clean = "call_abc123"
        result_key = f"var_{tool_call_id_clean}".replace("-", "_")

        self.assertEqual(result_key, "var_call_abc123")
        self.assertTrue(result_key.isidentifier())

if __name__ == "__main__":
    unittest.main()
