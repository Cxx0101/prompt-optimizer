# Sources and design notes

This skill is an original cross-agent implementation inspired by public prompt-engineering patterns and the ai-boost/awesome-prompts Generative Image Prompt Engineer concept. It does not reproduce that source prompt verbatim.

Primary standards and platform references used during design:

- Agent Skills open specification: https://agentskills.io/specification
- Anthropic Agent Skills overview and Claude Code skill guidance: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Anthropic skills examples: https://github.com/anthropics/skills
- OpenAI Codex / ChatGPT build-skills documentation: https://learn.chatgpt.com/docs/build-skills
- Hermes Skills System: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- OpenAI GPT Image model documentation: https://developers.openai.com/api/docs/models/gpt-image-2
- Midjourney parameter documentation: https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List
- Black Forest Labs FLUX prompting guide: https://docs.bfl.ai/guides/prompting_summary
- Google Gemini image-generation documentation: https://ai.google.dev/gemini-api/docs/image-generation
- Source inspiration: https://github.com/ai-boost/awesome-prompts/blob/main/prompts/generative_image_prompt_engineer.txt

Platform features and model parameters evolve. The adapters are intentionally written to prefer stable prompting behavior and to avoid asserting volatile syntax without a clear need.
