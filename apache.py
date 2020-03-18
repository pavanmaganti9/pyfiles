#!c:/Python27/python
print "Content-type: text/html"
print
print ("Pavan")
print "<br><br>"

$headers = getallheaders();
$payload = file_get_contents("php://input");
$webhook = new AuthnetWebhook(AUTHNET_SIGNATURE, $payload, $headers);
if ($webhook-&gt;isValid()) {
    // Access notification values
}

$headers = getallheaders();
$payload = file_get_contents("php://input");
$webhook = new AuthnetWebhook(AUTHNET_SIGNATURE, $payload, $headers);
if ($webhook-&gt;isValid()) {
    // Get the transaction ID
    $transactionId = $webhook-&gt;payload-&gt;id;
}

https://github.com/stymiee/authnetjson/blob/master/examples/reporting/getTransactionDetailsRequest.php
