import { TestBed } from "@angular/core/testing";

import { RpsService } from "./rps-service.service";

describe("RpsServiceService", () => {
  let service: RpsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RpsService);
  });

  it("should be created", () => {
    expect(service).toBeTruthy();
  });
});
