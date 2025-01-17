# EzsigntemplatepackageCreateObjectV1Response

Response for POST /1/object/ezsigntemplatepackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigntemplatepackageCreateObjectV1ResponseMPayload**](EzsigntemplatepackageCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_create_object_v1_response import EzsigntemplatepackageCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageCreateObjectV1Response from a JSON string
ezsigntemplatepackage_create_object_v1_response_instance = EzsigntemplatepackageCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackage_create_object_v1_response_dict = ezsigntemplatepackage_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackageCreateObjectV1Response from a dict
ezsigntemplatepackage_create_object_v1_response_from_dict = EzsigntemplatepackageCreateObjectV1Response.from_dict(ezsigntemplatepackage_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


