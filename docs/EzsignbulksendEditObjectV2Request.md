# EzsignbulksendEditObjectV2Request

Request for PUT /2/object/ezsignbulksend/{pkiEzsignbulksendID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignbulksend** | [**EzsignbulksendRequestCompoundV2**](EzsignbulksendRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_edit_object_v2_request import EzsignbulksendEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendEditObjectV2Request from a JSON string
ezsignbulksend_edit_object_v2_request_instance = EzsignbulksendEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendEditObjectV2Request.to_json())

# convert the object into a dict
ezsignbulksend_edit_object_v2_request_dict = ezsignbulksend_edit_object_v2_request_instance.to_dict()
# create an instance of EzsignbulksendEditObjectV2Request from a dict
ezsignbulksend_edit_object_v2_request_from_dict = EzsignbulksendEditObjectV2Request.from_dict(ezsignbulksend_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


