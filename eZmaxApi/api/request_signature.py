import hashlib
import hmac
from datetime import datetime, timezone
from typing import Dict, Optional, Union


class RequestSignature:

    @staticmethod
    def get_fingerprint_v1(
        authorization: str,
        date: str,
        method: str,
        url: str,
        body: str = "",
        expiration: Optional[int] = None,
    ) -> str:
        content_to_hash = f"{method}\n{url}\n{body}\n{authorization}\n{date}"
        if expiration is not None:
            content_to_hash += f"\n{expiration}"

        hashed_content = hashlib.sha256(content_to_hash.encode("utf-8")).hexdigest()
        return f"v1={hashed_content}"

    @staticmethod
    def get_signature_v1(
        authorization: str, date: str, fingerprint: str, secret: str
    ) -> str:
        content_to_sign = f"{fingerprint}{authorization}{date}"

        signature = hmac.new(
            secret.encode("utf-8"),
            content_to_sign.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        return f"v1={signature}"

    @staticmethod
    def get_headers_v1(
        authorization: str,
        secret: str,
        method: str,
        url: str,
        body: str = "",
        expiration: Optional[int] = None,
    ) -> Dict[str, Union[str, int]]:
        dt_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        fingerprint = RequestSignature.get_fingerprint_v1(
            authorization, dt_date, method, url, body, expiration
        )
        signature = RequestSignature.get_signature_v1(
            authorization, dt_date, fingerprint, secret
        )

        headers = {
            "Ezmax-Date": dt_date,
            "Ezmax-Fingerprint": fingerprint,
            "Ezmax-Signature": signature,
        }

        if expiration is not None:
            headers["Ezmax-Expiration"] = expiration

        return headers