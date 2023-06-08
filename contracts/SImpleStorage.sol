// SPDX-License-Identifier: MIT
pragma solidity >=0.8.8;

contract SimpleStorage {
    uint256 public  number;
    Person public person1 = Person({name:"NAme", age:45});

    struct Person{
        string name;
        uint256 age;
    }

    Person[] public people;
    function getNumber (uint256 _number) public {
        number = _number;
    }
    function retrieve() public view returns(uint256){
        return number;
    }

    function pureRetrieve() public pure returns(uint256){
        return 1+1;
    }

    function pushToPeople(string memory _name, uint256 _age) public{
        people.push(Person(_name, _age));
    }
}

//0xd9145CCE52D386f254917e481eB44e9943F39138 address of contract