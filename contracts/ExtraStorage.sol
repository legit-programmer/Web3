// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

import "contracts/SImpleStorage.sol";
contract ExtraStorage is SimpleStorage {
    function storeNumber(uint256 _number) public virtual override {
        number = _number+5;
    }
}
