
"use strict";

let Analog = require('./Analog.js');
let Digital = require('./Digital.js');
let ToolDataMsg = require('./ToolDataMsg.js');
let MasterboardDataMsg = require('./MasterboardDataMsg.js');
let IOStates = require('./IOStates.js');
let RobotModeDataMsg = require('./RobotModeDataMsg.js');
let RobotStateRTMsg = require('./RobotStateRTMsg.js');

module.exports = {
  Analog: Analog,
  Digital: Digital,
  ToolDataMsg: ToolDataMsg,
  MasterboardDataMsg: MasterboardDataMsg,
  IOStates: IOStates,
  RobotModeDataMsg: RobotModeDataMsg,
  RobotStateRTMsg: RobotStateRTMsg,
};
