pragma solidity =0.7.3;

contract MyFirstContract {

    uint256 number;


    function setNumber(uint256 num) public {
        number = num;
    }


    function getNumber() public view returns (uint256){
        return number;
    }

    function addNumber(uint256 _num) public view returns (uint256){
        return number + _num;
    }
}
