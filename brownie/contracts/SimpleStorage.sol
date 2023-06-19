// SPDX-License-Identifier: MIT
pragma solidity >=0.8.8;

contract SimpleStorage {
    uint256 public number;
    Person public person1 = Person({name: "NAme", age: 45});

    struct Person {
        string name;
        uint256 age;
    }

    mapping(string => uint256) public peopleInMap;

    Person[] public people;

    function storeNumber(uint256 _number) public virtual returns(uint256){
        number = _number;
        return number;
    }

    function retrieve() public view returns (uint256) {
        return number;
    }

    function pureRetrieve() public pure returns (uint256) {
        return 1 + 1;
    }

    //calldata: temporary and cannot modify, memory: temporary but can be modified, storage: not permenant and can be changed
    // structs, array and maps should have these keywords
    function pushToPeople(string memory _name, uint256 _age) public {
        people.push(Person(_name, _age));
        peopleInMap[_name] = _age;
    }
}

//0xd9145CCE52D386f254917e481eB44e9943F39138 address of contract
