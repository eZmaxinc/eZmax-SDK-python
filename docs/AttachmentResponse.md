# AttachmentResponse

An Attachment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_attachment_id** | **int** | The unique ID of the Attachment. | 
**fki_computer_id** | **int** | The unique ID of the Computer | [optional] 
**fki_adjustment_id** | **int** | The unique ID of the Adjustment | [optional] 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_commissionadvance_id** | **int** | The unique ID of the Commissionadvance | [optional] 
**fki_communication_id** | **int** | The unique ID of the Communication. | [optional] 
**fki_customer_id** | **int** | The unique ID of the Customer. | [optional] 
**fki_customertemplate_id** | **int** | The unique ID of the Customertemplate | [optional] 
**fki_deposit_id** | **int** | The unique ID of the Deposit | [optional] 
**fki_deposittransitcheque_id** | **int** | The unique ID of the Deposittransitcheque | [optional] 
**fki_electronicfundstransfer_id** | **int** | The unique ID of the Electronicfundstransfer | [optional] 
**fki_employee_id** | **int** | The unique ID of the Employee. | [optional] 
**fki_externalbroker_id** | **int** | The unique ID of the Externalbroker. | [optional] 
**fki_ezcomadvanceserver_id** | **int** | The unique ID of the Ezcomadvanceserver | [optional] 
**fki_ezcomcompany_id** | **int** | The unique ID of the Ezcomcompany | [optional] 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | [optional] 
**fki_ghacqcontract_id** | **int** | The unique ID of the Ghacqcontract | [optional] 
**fki_inscription_id** | **int** | The unique ID of the Inscription. | [optional] 
**fki_inscriptiontemp_id** | **int** | The unique ID of the Inscriptiontemp | [optional] 
**fki_inscriptionnotauthenticated_id** | **int** | The unique ID of the Inscriptionnotauthenticated. | [optional] 
**fki_invoice_id** | **int** | The unique ID of the Invoice. | [optional] 
**fki_buyercontract_id** | **int** | The unique ID of the Buyercontract | [optional] 
**fki_franchisebroker_id** | **int** | The unique ID of the Franchisebroker | [optional] 
**fki_franchiseagence_id** | **int** | The unique ID of the Franchiseagence | [optional] 
**fki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | [optional] 
**fki_franchisefranchise_id** | **int** | The unique ID of the Franchisefranchise | [optional] 
**fki_franchisecomplaint_id** | **int** | The unique ID of the Franchisecomplaint | [optional] 
**fki_lead_id** | **int** | The unique ID of the Lead | [optional] 
**fki_marketingprogram_id** | **int** | The unique ID of the Marketingprogram | [optional] 
**fki_marketingfollow_id** | **int** | The unique ID of the Marketingfollow | [optional] 
**fki_notary_id** | **int** | The unique ID of the Notary. | [optional] 
**fki_officetaxreport_id** | **int** | The unique ID of the Officetaxreport | [optional] 
**fki_otherincome_id** | **int** | The unique ID of the Otherincome | [optional] 
**fki_paymentpreparation_id** | **int** | The unique ID of the Paymentpreparation | [optional] 
**fki_purchase_id** | **int** | The unique ID of the Purchase | [optional] 
**fki_salary_id** | **int** | The unique ID of the Salary | [optional] 
**fki_supplier_id** | **int** | The unique ID of the Supplier. | [optional] 
**fki_tranqcontract_id** | **int** | The unique ID of the Tranqcontract | [optional] 
**fki_template_id** | **int** | The unique ID of the Template | [optional] 
**fki_inscriptionchecklist_id** | **int** | The unique ID of the Inscriptionchecklist | [optional] 
**fki_folder_id** | **int** | The unique ID of the Folder | [optional] 
**fki_rejectedoffertopurchase_id** | **int** | The unique ID of the Rejectedoffertopurchase | [optional] 
**fki_disclosure_id** | **int** | The unique ID of the Disclosure | [optional] 
**fki_reconciliation_id** | **int** | The unique ID of the Reconciliation | [optional] 
**fki_ezsigndocument_id_reference** | **int** | The unique ID of the Ezsigndocument | [optional] 
**e_attachment_documenttype** | [**FieldEAttachmentDocumenttype**](FieldEAttachmentDocumenttype.md) |  | 
**s_attachment_name** | **str** | The name of the Attachment | 
**e_attachment_privacy** | [**FieldEAttachmentPrivacy**](FieldEAttachmentPrivacy.md) |  | 
**fki_user_id_specific** | **int** | The unique ID of the User | [optional] 
**e_attachment_type** | [**FieldEAttachmentType**](FieldEAttachmentType.md) |  | 
**i_attachment_size** | **int** | The size of the Attachment | 
**i_attachment_ed_mmoduleflag** | **int** | The edmmoduleflag of the Attachment | [optional] 
**s_attachment_md5** | **str** | The md5 of the Attachment | 
**b_attachment_deleted** | **bool** | Whether if it&#39;s deleted | 
**b_attachment_valid** | **bool** | Whether if it&#39;s valid | 
**e_attachment_verified** | [**FieldEAttachmentVerified**](FieldEAttachmentVerified.md) |  | 
**t_attachment_rejectioncomment** | **str** | The rejectioncomment of the Attachment | [optional] 
**fki_user_id_owner** | **int** | The unique ID of the User | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.attachment_response import AttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentResponse from a JSON string
attachment_response_instance = AttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(AttachmentResponse.to_json())

# convert the object into a dict
attachment_response_dict = attachment_response_instance.to_dict()
# create an instance of AttachmentResponse from a dict
attachment_response_form_dict = attachment_response.from_dict(attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


