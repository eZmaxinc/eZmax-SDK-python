# EzsigntemplatepackagesignerCreateObjectV2Request

Request for POST /2/object/ezsigntemplatepackagesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerRequestCompoundV2]**](EzsigntemplatepackagesignerRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_create_object_v2_request import EzsigntemplatepackagesignerCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerCreateObjectV2Request from a JSON string
ezsigntemplatepackagesigner_create_object_v2_request_instance = EzsigntemplatepackagesignerCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerCreateObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_create_object_v2_request_dict = ezsigntemplatepackagesigner_create_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerCreateObjectV2Request from a dict
ezsigntemplatepackagesigner_create_object_v2_request_from_dict = EzsigntemplatepackagesignerCreateObjectV2Request.from_dict(ezsigntemplatepackagesigner_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


