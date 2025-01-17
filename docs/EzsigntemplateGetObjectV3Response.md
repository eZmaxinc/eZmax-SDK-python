# EzsigntemplateGetObjectV3Response

Response for GET /3/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplateGetObjectV3ResponseMPayload**](EzsigntemplateGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_object_v3_response import EzsigntemplateGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetObjectV3Response from a JSON string
ezsigntemplate_get_object_v3_response_instance = EzsigntemplateGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateGetObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplate_get_object_v3_response_dict = ezsigntemplate_get_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplateGetObjectV3Response from a dict
ezsigntemplate_get_object_v3_response_from_dict = EzsigntemplateGetObjectV3Response.from_dict(ezsigntemplate_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


