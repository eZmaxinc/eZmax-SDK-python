# EzsigntemplatepackagesignerEditObjectV2Request

Request for PUT /2/object/ezsigntemplatepackagesigner/{pkiEzsigntemplatepackagesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatepackagesigner** | [**EzsigntemplatepackagesignerRequestCompoundV2**](EzsigntemplatepackagesignerRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_edit_object_v2_request import EzsigntemplatepackagesignerEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerEditObjectV2Request from a JSON string
ezsigntemplatepackagesigner_edit_object_v2_request_instance = EzsigntemplatepackagesignerEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerEditObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_edit_object_v2_request_dict = ezsigntemplatepackagesigner_edit_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerEditObjectV2Request from a dict
ezsigntemplatepackagesigner_edit_object_v2_request_from_dict = EzsigntemplatepackagesignerEditObjectV2Request.from_dict(ezsigntemplatepackagesigner_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


