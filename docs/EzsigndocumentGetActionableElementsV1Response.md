# EzsigndocumentGetActionableElementsV1Response

Response for GET /1/object/ezsigndocument/{pkiEzsigndocumentID}/getActionableElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigndocumentGetActionableElementsV1ResponseMPayload**](EzsigndocumentGetActionableElementsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_actionable_elements_v1_response import EzsigndocumentGetActionableElementsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetActionableElementsV1Response from a JSON string
ezsigndocument_get_actionable_elements_v1_response_instance = EzsigndocumentGetActionableElementsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetActionableElementsV1Response.to_json())

# convert the object into a dict
ezsigndocument_get_actionable_elements_v1_response_dict = ezsigndocument_get_actionable_elements_v1_response_instance.to_dict()
# create an instance of EzsigndocumentGetActionableElementsV1Response from a dict
ezsigndocument_get_actionable_elements_v1_response_from_dict = EzsigndocumentGetActionableElementsV1Response.from_dict(ezsigndocument_get_actionable_elements_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


