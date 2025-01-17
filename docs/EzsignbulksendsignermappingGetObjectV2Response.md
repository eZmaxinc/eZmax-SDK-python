# EzsignbulksendsignermappingGetObjectV2Response

Response for GET /2/object/ezsignbulksendsignermapping/{pkiEzsignbulksendsignermappingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignbulksendsignermappingGetObjectV2ResponseMPayload**](EzsignbulksendsignermappingGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendsignermapping_get_object_v2_response import EzsignbulksendsignermappingGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendsignermappingGetObjectV2Response from a JSON string
ezsignbulksendsignermapping_get_object_v2_response_instance = EzsignbulksendsignermappingGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendsignermappingGetObjectV2Response.to_json())

# convert the object into a dict
ezsignbulksendsignermapping_get_object_v2_response_dict = ezsignbulksendsignermapping_get_object_v2_response_instance.to_dict()
# create an instance of EzsignbulksendsignermappingGetObjectV2Response from a dict
ezsignbulksendsignermapping_get_object_v2_response_from_dict = EzsignbulksendsignermappingGetObjectV2Response.from_dict(ezsignbulksendsignermapping_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


