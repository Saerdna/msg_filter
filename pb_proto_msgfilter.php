<?php
/**
 * Auto generated from msgfilter.proto at 2015-02-28 15:12:34
 */

/**
 * MsgFilterRequest message
 */
class MsgFilterRequest extends \ProtobufMessage
{
    /* Field index constants */
    const TYPE = 1;
    const MSG = 2;

    /* @var array Field descriptors */
    protected static $fields = array(
        self::TYPE => array(
            'name' => 'type',
            'required' => true,
            'type' => 5,
        ),
        self::MSG => array(
            'name' => 'msg',
            'required' => true,
            'type' => 7,
        ),
    );

    /**
     * Constructs new message container and clears its internal state
     *
     * @return null
     */
    public function __construct()
    {
        $this->reset();
    }

    /**
     * Clears message values and sets default ones
     *
     * @return null
     */
    public function reset()
    {
        $this->values[self::TYPE] = null;
        $this->values[self::MSG] = null;
    }

    /**
     * Returns field descriptors
     *
     * @return array
     */
    public function fields()
    {
        return self::$fields;
    }

    /**
     * Sets value of 'type' property
     *
     * @param int $value Property value
     *
     * @return null
     */
    public function setType($value)
    {
        return $this->set(self::TYPE, $value);
    }

    /**
     * Returns value of 'type' property
     *
     * @return int
     */
    public function getType()
    {
        return $this->get(self::TYPE);
    }

    /**
     * Sets value of 'msg' property
     *
     * @param string $value Property value
     *
     * @return null
     */
    public function setMsg($value)
    {
        return $this->set(self::MSG, $value);
    }

    /**
     * Returns value of 'msg' property
     *
     * @return string
     */
    public function getMsg()
    {
        return $this->get(self::MSG);
    }
}

/**
 * MsgFilterResponse message
 */
class MsgFilterResponse extends \ProtobufMessage
{
    /* Field index constants */
    const ERROR_CODE = 1;
    const DESC = 2;
    const RET = 3;

    /* @var array Field descriptors */
    protected static $fields = array(
        self::ERROR_CODE => array(
            'name' => 'error_code',
            'required' => true,
            'type' => 5,
        ),
        self::DESC => array(
            'name' => 'desc',
            'required' => true,
            'type' => 7,
        ),
        self::RET => array(
            'name' => 'ret',
            'required' => true,
            'type' => 5,
        ),
    );

    /**
     * Constructs new message container and clears its internal state
     *
     * @return null
     */
    public function __construct()
    {
        $this->reset();
    }

    /**
     * Clears message values and sets default ones
     *
     * @return null
     */
    public function reset()
    {
        $this->values[self::ERROR_CODE] = null;
        $this->values[self::DESC] = null;
        $this->values[self::RET] = null;
    }

    /**
     * Returns field descriptors
     *
     * @return array
     */
    public function fields()
    {
        return self::$fields;
    }

    /**
     * Sets value of 'error_code' property
     *
     * @param int $value Property value
     *
     * @return null
     */
    public function setErrorCode($value)
    {
        return $this->set(self::ERROR_CODE, $value);
    }

    /**
     * Returns value of 'error_code' property
     *
     * @return int
     */
    public function getErrorCode()
    {
        return $this->get(self::ERROR_CODE);
    }

    /**
     * Sets value of 'desc' property
     *
     * @param string $value Property value
     *
     * @return null
     */
    public function setDesc($value)
    {
        return $this->set(self::DESC, $value);
    }

    /**
     * Returns value of 'desc' property
     *
     * @return string
     */
    public function getDesc()
    {
        return $this->get(self::DESC);
    }

    /**
     * Sets value of 'ret' property
     *
     * @param int $value Property value
     *
     * @return null
     */
    public function setRet($value)
    {
        return $this->set(self::RET, $value);
    }

    /**
     * Returns value of 'ret' property
     *
     * @return int
     */
    public function getRet()
    {
        return $this->get(self::RET);
    }
}
