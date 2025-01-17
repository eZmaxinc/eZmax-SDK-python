# EzsigndocumentGetObjectV2Response

Response for GET /2/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigndocumentGetObjectV2ResponseMPayload**](EzsigndocumentGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_object_v2_response import EzsigndocumentGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetObjectV2Response from a JSON string
ezsigndocument_get_object_v2_response_instance = EzsigndocumentGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetObjectV2Response.to_json())

# convert the object into a dict
ezsigndocument_get_object_v2_response_dict = ezsigndocument_get_object_v2_response_instance.to_dict()
# create an instance of EzsigndocumentGetObjectV2Response from a dict
ezsigndocument_get_object_v2_response_from_dict = EzsigndocumentGetObjectV2Response.from_dict(ezsigndocument_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


