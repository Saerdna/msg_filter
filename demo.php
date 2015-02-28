<?php
require_once 'pb_proto_msgfilter.php';
class MsgFilter
{
    private $_sock;
    private $_ip;
    private $_port;
    public function init($ip = "127.0.0.1", $port = "8081"){
        $this->_ip = $ip;
        $this->_port = $port;
    }
    public function filter($type, $msg){
        $this->_sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        $con = socket_connect($this->_sock, $this->_ip, $this->_port);
        $req = new MsgFilterRequest();
        $req->setType($type);
        $req->setMsg($msg);
        $packed = $req->serializeToString();
        socket_write($this->_sock, $packed);
        $buf = socket_read($this->_sock, 1024);
        $resp = new MsgFilterResponse();
        try{
            $resp->parseFromString($buf);
        }catch(Exception $e){
            echo "bad";           
        }
        if($resp->getErrorCode() == 0){
            return $resp->getRet();
        }
        return false;
    }       
}

$obj = new MsgFilter();
$obj->init();
echo $obj->filter(0, "apple");
echo $obj->filter(0, "中国人");
echo $obj->filter(0, "共产党");
echo $obj->filter(0, "中国共21产党");
