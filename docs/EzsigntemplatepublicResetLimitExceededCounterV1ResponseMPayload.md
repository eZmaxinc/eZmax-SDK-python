# EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}/resetLimitExceededCounter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_ezsigntemplatepublic_limitexceededsince** | **str** | The limitexceededsince of the Ezsigntemplatepublic | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_reset_limit_exceeded_counter_v1_response_m_payload import EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload from a JSON string
ezsigntemplatepublic_reset_limit_exceeded_counter_v1_response_m_payload_instance = EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload.to_json())

# convert the object into a dict
ezsigntemplatepublic_reset_limit_exceeded_counter_v1_response_m_payload_dict = ezsigntemplatepublic_reset_limit_exceeded_counter_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload from a dict
ezsigntemplatepublic_reset_limit_exceeded_counter_v1_response_m_payload_from_dict = EzsigntemplatepublicResetLimitExceededCounterV1ResponseMPayload.from_dict(ezsigntemplatepublic_reset_limit_exceeded_counter_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


