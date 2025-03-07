# EzsigndocumentPrefillEzsignformV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/prefillEzsignform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_prefillezsignformvalue** | [**List[CustomPrefillEzsignformValueRequest]**](CustomPrefillEzsignformValueRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_prefill_ezsignform_v1_request import EzsigndocumentPrefillEzsignformV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentPrefillEzsignformV1Request from a JSON string
ezsigndocument_prefill_ezsignform_v1_request_instance = EzsigndocumentPrefillEzsignformV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentPrefillEzsignformV1Request.to_json())

# convert the object into a dict
ezsigndocument_prefill_ezsignform_v1_request_dict = ezsigndocument_prefill_ezsignform_v1_request_instance.to_dict()
# create an instance of EzsigndocumentPrefillEzsignformV1Request from a dict
ezsigndocument_prefill_ezsignform_v1_request_from_dict = EzsigndocumentPrefillEzsignformV1Request.from_dict(ezsigndocument_prefill_ezsignform_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


