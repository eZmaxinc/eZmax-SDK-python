# EzsigntemplateEditObjectV2Request

Request for PUT /2/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplate** | [**EzsigntemplateRequestCompoundV2**](EzsigntemplateRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_edit_object_v2_request import EzsigntemplateEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateEditObjectV2Request from a JSON string
ezsigntemplate_edit_object_v2_request_instance = EzsigntemplateEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateEditObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplate_edit_object_v2_request_dict = ezsigntemplate_edit_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplateEditObjectV2Request from a dict
ezsigntemplate_edit_object_v2_request_form_dict = ezsigntemplate_edit_object_v2_request.from_dict(ezsigntemplate_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


