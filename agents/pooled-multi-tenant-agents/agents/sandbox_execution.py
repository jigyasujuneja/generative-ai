# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=line-too-long

"""Public backward-compatible facade for Agent Sandbox in Gemini (`agents.sandbox` subpackage)."""

from __future__ import annotations

import google.auth
import httpx

from agents.sandbox import _FORBIDDEN_CODE_SUBSTRINGS
from agents.sandbox import _FORBIDDEN_ENV_KEYS
from agents.sandbox import DEFAULT_SANDBOX_TTL_SECONDS
from agents.sandbox import ENTERPRISE_MAX_ACTIVE_SANDBOXES
from agents.sandbox import MAX_SANDBOX_CODE_CHARS
from agents.sandbox import MAX_SANDBOX_TTL_SECONDS
from agents.sandbox import STANDARD_MAX_ACTIVE_SANDBOXES
from agents.sandbox import GeminiAgentSandboxManager
from agents.sandbox import HermeticZeroCredentialSandboxBackend
from agents.sandbox import LiveGeminiAgentSandboxClient
from agents.sandbox import SandboxBackendClient
from agents.sandbox import SandboxBackendCreateResult
from agents.sandbox import SandboxBackendExecutionResult
from agents.sandbox import SandboxEnvironmentRecord
from agents.sandbox import SandboxLanguage
from agents.sandbox import SandboxLifecycleState
from agents.sandbox import SandboxTaintTuple
from agents.sandbox import SandboxUnavailableError
from agents.sandbox import _assert_synchronous_backend
from agents.sandbox import _control_plane_adc_headers
from agents.sandbox import _decode_chunk_output_item
from agents.sandbox import assert_zero_credentials_and_egress_safe

__all__ = [
    "DEFAULT_SANDBOX_TTL_SECONDS",
    "ENTERPRISE_MAX_ACTIVE_SANDBOXES",
    "MAX_SANDBOX_CODE_CHARS",
    "MAX_SANDBOX_TTL_SECONDS",
    "STANDARD_MAX_ACTIVE_SANDBOXES",
    "_FORBIDDEN_CODE_SUBSTRINGS",
    "_FORBIDDEN_ENV_KEYS",
    "GeminiAgentSandboxManager",
    "HermeticZeroCredentialSandboxBackend",
    "LiveGeminiAgentSandboxClient",
    "SandboxBackendClient",
    "SandboxBackendCreateResult",
    "SandboxBackendExecutionResult",
    "SandboxEnvironmentRecord",
    "SandboxLanguage",
    "SandboxLifecycleState",
    "SandboxTaintTuple",
    "SandboxUnavailableError",
    "_assert_synchronous_backend",
    "_control_plane_adc_headers",
    "_decode_chunk_output_item",
    "assert_zero_credentials_and_egress_safe",
    "google",
    "httpx",
]
