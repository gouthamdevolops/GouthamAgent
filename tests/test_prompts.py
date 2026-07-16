import sys
import os
import unittest

# Append Source_Code to path so tests can import from it
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Source_Code"))

from prompt_builder import init_messages, GPT_TOOL_CALL_INSTRUCTIONS, GEMINI_TOOL_CALL_INSTRUCTIONS, CLAUDE_TOOL_CALL_INSTRUCTIONS

class TestPromptBuilding(unittest.TestCase):
    def test_init_messages_gpt(self):
        """
        Test that prompt_builder selects the correct system prompt settings for GPT models.
        """
        user_query = "Find total stars."
        db_description = "A sqlite database."
        deployment = "gpt-4o-mini"
        
        messages = init_messages(user_query, db_description, deployment)
        
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["role"], "user")
        
        system_content = messages[0]["content"]
        self.assertIn(GPT_TOOL_CALL_INSTRUCTIONS, system_content)
        self.assertNotIn(GEMINI_TOOL_CALL_INSTRUCTIONS, system_content)

    def test_init_messages_gemini(self):
        """
        Test that prompt_builder selects the correct system prompt settings for Gemini models.
        """
        user_query = "Find total stars."
        db_description = "A sqlite database."
        deployment = "google/gemini-2-9b-it:free"
        
        messages = init_messages(user_query, db_description, deployment)
        
        system_content = messages[0]["content"]
        self.assertIn(GEMINI_TOOL_CALL_INSTRUCTIONS, system_content)
        self.assertNotIn(GPT_TOOL_CALL_INSTRUCTIONS, system_content)

    def test_init_messages_claude(self):
        """
        Test that prompt_builder selects the correct system prompt settings for Claude models.
        """
        user_query = "Find total stars."
        db_description = "A sqlite database."
        deployment = "anthropic/claude-3-haiku"
        
        messages = init_messages(user_query, db_description, deployment)
        
        system_content = messages[0]["content"]
        self.assertIn(CLAUDE_TOOL_CALL_INSTRUCTIONS, system_content)

if __name__ == "__main__":
    unittest.main()
