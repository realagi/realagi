---
title: Execute Prompts with Discord and Repository Context
---

## Goal
Enable the bot to execute any prompt using both the current Discord channel context and the repository contents, running within the OpenHands runtime on Kubernetes and leveraging the Codex API.

## Plan
1. **Kubernetes Runtime Setup**
   - Deploy the OpenHands runtime to the Kubernetes cluster.
   - Configure persistent storage for cloning and updating the active repository per request.

2. **Discord Context Integration**
   - Implement a service that receives events/messages from Discord channels.
   - Collect recent channel history and pass it as contextual input when executing prompts.

3. **Repository Mounting**
   - For each request, mount or sync the referenced repository into the runtime.
   - Ensure changes made by the agent are persisted back to the repository's run workspace.

4. **Codex API Execution**
   - Forward combined context (Discord messages + repository files) to the Codex API for code generation or command execution.
   - Stream Codex responses back to the Discord channel.

5. **Microagent Support**
   - If the bot cannot fulfill a request, trigger an OpenHands microagent tailored to the required domain or workflow.

6. **Next Steps Tracking**
   - Track refinements and implementation tasks in this `docs/devplans` directory.

