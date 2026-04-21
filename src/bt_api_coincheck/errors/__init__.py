from __future__ import annotations

from typing import Any

from bt_api_base.error import ErrorCategory, ErrorTranslator, UnifiedError, UnifiedErrorCode


class CoincheckErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, raw_error: dict[str, Any], venue: str) -> UnifiedError | None:
        message = str(raw_error.get("error", raw_error.get("message", "")))
        lower = message.lower()

        if "balance" in lower or "insufficient" in lower:
            error_code = UnifiedErrorCode.INSUFFICIENT_BALANCE
            category = ErrorCategory.BUSINESS
        elif "order" in lower and "not found" in lower:
            error_code = UnifiedErrorCode.ORDER_NOT_FOUND
            category = ErrorCategory.BUSINESS
        elif "duplicate" in lower:
            error_code = UnifiedErrorCode.DUPLICATE_ORDER
            category = ErrorCategory.BUSINESS
        elif "rate" in lower or "limit" in lower:
            error_code = UnifiedErrorCode.RATE_LIMIT_EXCEEDED
            category = ErrorCategory.RATE_LIMIT
        elif "auth" in lower or "key" in lower or "signature" in lower:
            error_code = UnifiedErrorCode.INVALID_API_KEY
            category = ErrorCategory.AUTH
        else:
            return super().translate(raw_error, venue)

        return UnifiedError(
            code=error_code,
            category=category,
            venue=venue,
            message=message or error_code.name,
            original_error=str(raw_error),
            context={"raw_response": raw_error},
        )
