# EzsigntemplatesignerCreateObjectV2Request

Request for POST /2/object/ezsigntemplatesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerRequestCompoundV2]**](EzsigntemplatesignerRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_create_object_v2_request import EzsigntemplatesignerCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerCreateObjectV2Request from a JSON string
ezsigntemplatesigner_create_object_v2_request_instance = EzsigntemplatesignerCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerCreateObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplatesigner_create_object_v2_request_dict = ezsigntemplatesigner_create_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplatesignerCreateObjectV2Request from a dict
ezsigntemplatesigner_create_object_v2_request_from_dict = EzsigntemplatesignerCreateObjectV2Request.from_dict(ezsigntemplatesigner_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


