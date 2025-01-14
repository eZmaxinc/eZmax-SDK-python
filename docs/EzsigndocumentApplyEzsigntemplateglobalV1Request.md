# EzsigndocumentApplyEzsigntemplateglobalV1Request

Request for POST /1/object/ezsigndocument/{pkiEzsigndocumentID}/applyEzsigntemplateglobal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsigntemplateglobal_id** | **int** | The unique ID of the Ezsigntemplateglobal | 
**a_s_ezsigntemplateglobalsigner** | **List[str]** |  | 
**a_pki_ezsignfoldersignerassociation_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_apply_ezsigntemplateglobal_v1_request import EzsigndocumentApplyEzsigntemplateglobalV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentApplyEzsigntemplateglobalV1Request from a JSON string
ezsigndocument_apply_ezsigntemplateglobal_v1_request_instance = EzsigndocumentApplyEzsigntemplateglobalV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentApplyEzsigntemplateglobalV1Request.to_json())

# convert the object into a dict
ezsigndocument_apply_ezsigntemplateglobal_v1_request_dict = ezsigndocument_apply_ezsigntemplateglobal_v1_request_instance.to_dict()
# create an instance of EzsigndocumentApplyEzsigntemplateglobalV1Request from a dict
ezsigndocument_apply_ezsigntemplateglobal_v1_request_from_dict = EzsigndocumentApplyEzsigntemplateglobalV1Request.from_dict(ezsigndocument_apply_ezsigntemplateglobal_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


