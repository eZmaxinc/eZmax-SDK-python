# EzsignbulksendReorderV1Request

Request for POST /1/object/ezsignbulksend/{pkiEzsignbulksendID}/reorder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsignbulksenddocumentmapping_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_reorder_v1_request import EzsignbulksendReorderV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendReorderV1Request from a JSON string
ezsignbulksend_reorder_v1_request_instance = EzsignbulksendReorderV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendReorderV1Request.to_json())

# convert the object into a dict
ezsignbulksend_reorder_v1_request_dict = ezsignbulksend_reorder_v1_request_instance.to_dict()
# create an instance of EzsignbulksendReorderV1Request from a dict
ezsignbulksend_reorder_v1_request_form_dict = ezsignbulksend_reorder_v1_request.from_dict(ezsignbulksend_reorder_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


