# EzsignbulksendCreateObjectV1Request

Request for POST /1/object/ezsignbulksend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignbulksend** | [**List[EzsignbulksendRequestCompound]**](EzsignbulksendRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_create_object_v1_request import EzsignbulksendCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendCreateObjectV1Request from a JSON string
ezsignbulksend_create_object_v1_request_instance = EzsignbulksendCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendCreateObjectV1Request.to_json()

# convert the object into a dict
ezsignbulksend_create_object_v1_request_dict = ezsignbulksend_create_object_v1_request_instance.to_dict()
# create an instance of EzsignbulksendCreateObjectV1Request from a dict
ezsignbulksend_create_object_v1_request_form_dict = ezsignbulksend_create_object_v1_request.from_dict(ezsignbulksend_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


