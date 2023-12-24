# EzsignbulksendEditObjectV1Request

Request for PUT /1/object/ezsignbulksend/{pkiEzsignbulksendID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksend** | [**EzsignbulksendRequestCompound**](EzsignbulksendRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_edit_object_v1_request import EzsignbulksendEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendEditObjectV1Request from a JSON string
ezsignbulksend_edit_object_v1_request_instance = EzsignbulksendEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendEditObjectV1Request.to_json()

# convert the object into a dict
ezsignbulksend_edit_object_v1_request_dict = ezsignbulksend_edit_object_v1_request_instance.to_dict()
# create an instance of EzsignbulksendEditObjectV1Request from a dict
ezsignbulksend_edit_object_v1_request_form_dict = ezsignbulksend_edit_object_v1_request.from_dict(ezsignbulksend_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


