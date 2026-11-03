# DocumenttypeListElement

A Documenttype List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttype_id** | **int** | The unique ID of the Documenttype | 
**s_documenttype_name_x** | **str** | The name of the Documenttype in the language of the requester | 
**s_documenttype_defaultfilename** | **str** | The defaultfilename of the Documenttype | 
**b_documenttype_showagent** | **bool** | Whether if it&#39;s an showagent | 
**b_documenttype_isactive** | **bool** | Whether the documenttype is active or not | 
**b_documenttype_isrequired** | **bool** | Whether if it&#39;s an isrequired | 
**b_documenttype_sale** | **bool** | Whether if it&#39;s an sale | 
**b_documenttype_rental** | **bool** | Whether if it&#39;s an rental | 
**b_documenttype_reference** | **bool** | Whether if it&#39;s an reference | 
**b_documenttype_mortgagereference** | **bool** | Whether if it&#39;s an mortgagereference | 
**b_documenttype_evaluation** | **bool** | Whether if it&#39;s an evaluation | 
**b_documenttype_consultation** | **bool** | Whether if it&#39;s an consultation | 
**b_documenttype_otherservices** | **bool** | Whether if it&#39;s an otherservices | 
**b_documenttype_foreclosedsale** | **bool** | Whether if it&#39;s an foreclosedsale | 
**b_documenttype_commercialfunding** | **bool** | Whether if it&#39;s an commercialfunding | 
**b_documenttype_canafe** | **bool** | Whether if it&#39;s an canafe | 
**e_documenttype_ezcom** | [**FieldEDocumenttypeEzcom**](FieldEDocumenttypeEzcom.md) |  | [optional] 
**e_documenttype_privacydefault** | [**FieldEDocumenttypePrivacydefault**](FieldEDocumenttypePrivacydefault.md) |  | 
**e_documenttype_statusdefault** | [**FieldEDocumenttypeStatusdefault**](FieldEDocumenttypeStatusdefault.md) |  | 
**e_documenttype_salebyowner** | [**FieldEDocumenttypeSalebyowner**](FieldEDocumenttypeSalebyowner.md) |  | 
**e_documenttype_saledisplaybyrole** | [**FieldEDocumenttypeSaledisplaybyrole**](FieldEDocumenttypeSaledisplaybyrole.md) |  | 
**e_documenttype_transactiontype** | [**FieldEDocumenttypeTransactiontype**](FieldEDocumenttypeTransactiontype.md) |  | 
**e_documenttype_repossession** | [**FieldEDocumenttypeRepossession**](FieldEDocumenttypeRepossession.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_list_element import DocumenttypeListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeListElement from a JSON string
documenttype_list_element_instance = DocumenttypeListElement.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeListElement.to_json())

# convert the object into a dict
documenttype_list_element_dict = documenttype_list_element_instance.to_dict()
# create an instance of DocumenttypeListElement from a dict
documenttype_list_element_from_dict = DocumenttypeListElement.from_dict(documenttype_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


