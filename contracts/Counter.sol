pragma solidity ^0.8.0;

//SPDX-License-Identifier: Unlicense

import "./SafeMath.sol";

contract Counter {
    using SafeMath for uint256;
    uint256 public count;

    function increment() public {
        count = SafeMath.add(count, 1);
    }

    function decrement() public {
        count = SafeMath.sub(count, 1);
    }

    function reset() public {
        count = 0;
    }

    function getCount() public view returns (uint256) {
        return count;
    }

    function setCount(uint256 _count) public {
        count = _count;
    }
}
