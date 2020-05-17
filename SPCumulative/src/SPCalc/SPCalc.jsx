import "./SPCalc.css";
import React from "react";
import "rc-slider/assets/index.css";
import DispTable from "../dispTable";

const Slider = require("rc-slider");
const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);

function template() {
  return (
    <div className="spcalc">
      {"Year Range: "}
      {this.state.startDate}
      {" - "}
      {this.state.endDate}
      <Range
        min={this.state.beginRangeYear}
        max={this.state.endRangeYear}
        defaultValue={[this.state.startDate, this.state.endDate]}
        onAfterChange={(value) =>
          this.setState({ startDate: value[0], endDate: value[1] })
        }
        pushable={true}
      />

      <DispTable
        data={this.state.data}
        startDate={this.state.startDate}
        endDate={this.state.endDate}
      />
    </div>
  );
}

export default template;
