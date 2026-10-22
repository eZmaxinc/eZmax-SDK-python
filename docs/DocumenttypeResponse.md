# DocumenttypeResponse

A Documenttype Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttype_id** | **int** | The unique ID of the Documenttype | 
**obj_documenttype_name** | [**MultilingualDocumenttypeName**](MultilingualDocumenttypeName.md) |  | 
**s_documenttype_defaultfilename** | **str** | The defaultfilename of the Documenttype | 
**b_documenttype_showagent** | **bool** | Whether if it&#39;s an showagent | 
**b_documenttype_isactive** | **bool** | Whether the documenttype is active or not | 
**b_documenttype_isrequired** | **bool** | Whether if it&#39;s an isrequired | 
**b_documenttype_sale** | **bool** | Whether if it&#39;s an sale | [optional] 
**b_documenttype_rental** | **bool** | Whether if it&#39;s an rental | [optional] 
**b_documenttype_reference** | **bool** | Whether if it&#39;s an reference | [optional] 
**b_documenttype_mortgagereference** | **bool** | Whether if it&#39;s an mortgagereference | [optional] 
**b_documenttype_evaluation** | **bool** | Whether if it&#39;s an evaluation | [optional] 
**b_documenttype_consultation** | **bool** | Whether if it&#39;s an consultation | [optional] 
**b_documenttype_otherservices** | **bool** | Whether if it&#39;s an otherservices | [optional] 
**b_documenttype_foreclosedsale** | **bool** | Whether if it&#39;s an foreclosedsale | [optional] 
**b_documenttype_commercialfunding** | **bool** | Whether if it&#39;s an commercialfunding | [optional] 
**b_documenttype_canafe** | **bool** | Whether if it&#39;s an canafe | [optional] 
**e_documenttype_ezcom** | [**FieldEDocumenttypeEzcom**](FieldEDocumenttypeEzcom.md) |  | [optional] 
**e_documenttype_privacydefault** | [**FieldEDocumenttypePrivacydefault**](FieldEDocumenttypePrivacydefault.md) |  | [optional] 
**e_documenttype_statusdefault** | [**FieldEDocumenttypeStatusdefault**](FieldEDocumenttypeStatusdefault.md) |  | [optional] 
**e_documenttype_salebyowner** | [**FieldEDocumenttypeSalebyowner**](FieldEDocumenttypeSalebyowner.md) |  | [optional] 
**e_documenttype_saledisplaybyrole** | [**FieldEDocumenttypeSaledisplaybyrole**](FieldEDocumenttypeSaledisplaybyrole.md) |  | [optional] 
**e_documenttype_transactiontype** | [**FieldEDocumenttypeTransactiontype**](FieldEDocumenttypeTransactiontype.md) |  | [optional] 
**e_documenttype_repossession** | [**FieldEDocumenttypeRepossession**](FieldEDocumenttypeRepossession.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.documenttype_response import DocumenttypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeResponse from a JSON string
documenttype_response_instance = DocumenttypeResponse.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeResponse.to_json())

# convert the object into a dict
documenttype_response_dict = documenttype_response_instance.to_dict()
# create an instance of DocumenttypeResponse from a dict
documenttype_response_from_dict = DocumenttypeResponse.from_dict(documenttype_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


