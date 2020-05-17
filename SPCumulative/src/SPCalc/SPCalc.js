import React from "react";
import template from "./SPCalc.jsx";

class SPCalc extends React.Component {
  constructor(props) {
    super(props);

    let data = {};

    for (let i = 0; i < this.props.data.length; i++) {
      data[this.props.data[i].year] = this.props.data[i].totalReturn;
    }

    this.state = {
      data: data,
      startDate: this.props.data[10].year,
      endDate: this.props.data[0].year,
      beginRangeYear: this.props.data[this.props.data.length - 1].year,
      endRangeYear: this.props.data[0].year,
    };
  }

  handler(beginDate, finishDate) {
    this.setState({ startDate: beginDate, endDate: finishDate });
  }

  render() {
    return template.call(this);
  }
}

export default SPCalc;
