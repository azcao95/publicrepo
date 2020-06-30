import { Component, OnInit } from "@angular/core";
import { RpsService } from "../rps-service.service";

@Component({
  selector: "app-game",
  templateUrl: "./game.component.html",
  styleUrls: ["./game.component.css"],
})
export class GameComponent implements OnInit {
  playerScore: number;
  cpuScore: number;

  gameOver: Boolean;

  computerChoice: String;
  selectionLockedIn: Boolean;

  selectionString: String;
  result: String;

  constructor(private rpsService: RpsService) {}

  selectRock() {
    this.selectionString = "rock";
  }

  selectScissors() {
    this.selectionString = "scissors";
  }

  selectPaper() {
    this.selectionString = "paper";
  }

  isSubmitDisabled() {
    return this.gameOver === true || this.selectionString === "";
  }

  isSelectionLockedIn() {
    return this.selectionLockedIn;
  }

  isResultHidden() {
    return !this.gameOver;
  }

  resetGame() {
    this.selectionLockedIn = false;
    this.gameOver = false;
    this.selectionString = "";
  }

  onClickSubmit() {
    this.selectionLockedIn = true;

    return this.rpsService.getResponse(this.selectionString).subscribe(
      (response) => {
        this.gameOver = true;
        if (response.body["result"] === "win") {
          this.playerScore += 1;
        } else if (response.body["result"] === "lose") {
          this.cpuScore += 1;
        }

        this.computerChoice = response.body["computerChoice"];
        this.result = response.body["result"];
      },
      (response) => {
        this.gameOver = true;
        this.result = "An Error has occurred: " + response.status;
      }
    );
  }

  ngOnInit() {
    this.playerScore = 0;
    this.cpuScore = 0;
    this.gameOver = false;
    this.selectionLockedIn = false;
    this.selectionString = "";
  }
}
