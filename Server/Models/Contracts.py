from ormar import Text, Integer, Float

from Server.Models.BaseModel import BaseModel


class Contracts(BaseModel):
    Serial: str = Text(primary_key=True)
    NameEntity: str = Text()
    NitEntity: int = Integer()
    EntityCode: int = Integer()
    Department: str = Text()
    City: str = Text()
    Location: str = Text()
    Order: str = Text()
    Sector: str = Text()
    Branch: str = Text()
    CentralEntity: str = Text()
    ProcessPurchase: str = Text()
    SerialContract: str = Text()
    ReferenceContract: str = Text()
    StateContract: str = Text()
    CodeCategoryMain: str = Text()
    DescriptionProcess: str = Text()
    TypeContract: str = Text()
    ContractingMode: str = Text()
    JustifyContractingMode: str = Text()
    DateSign: str | None = Text(nullable=True)
    DateStartContract: str | None = Text(nullable=True)
    DateEndContract: str | None = Text(nullable=True)
    DateStartExecution: str | None = Text(nullable=True)
    DateEndExecution: str | None = Text(nullable=True)
    DeliveryConditions: str = Text()
    ProviderTypeDocument: str = Text()
    ProviderDocument: str = Text()
    ProviderAwarder: str = Text()
    IsGroup: str = Text()
    IsPyme: str = Text()
    EnableAdvancePayment: str = Text()
    Liquidation: str = Text()
    EnvironmentalObligation: str = Text()
    PostConsumerObligation: str = Text()
    Reversal: str = Text()
    ValueContract: int = Integer()
    ValueEnableAdvancePayment: int = Integer()
    ValueInvoice: int = Integer()
    ValuePendingPayment: int = Integer()
    ValuePaid: int = Integer()
    ValueAmortized: int = Integer()
    ValuePendingAmortized: int = Integer()
    ValuePendingExecution: int = Integer()
    StateBankOfNationalInvestmentProjects: str = Text()
    CodeBankOfNationalInvestmentProjects: str = Text()
    YearBankOfNationalInvestmentProjects: str = Text()
    BalanceCertificateOfBudgetaryAvailability: float = Float()
    BalanceVigence: int = Integer()
    IsPostConflict: str = Text()
    ProcessUrl: str = Text()
    ExpenseDestination: str = Text()
    OrigenResources: str = Text()
    DaysAdded: int = Integer()
    PointsOfTheAgreement: str = Text()
    PillarsOfTheAgreement: str = Text()
    LegalRepresentativeName: str = Text()
    LegalRepresentativeNationality: str = Text()
    LegalRepresentativeTypeIdentification: str = Text()
    LegalRepresentativeGender: str = Text()
    GeneralBudgetOfNation: int = Integer()
    GeneralParticipationSystem: int = Integer()
    GeneralRoyaltiesSystem: int = Integer()
    ResourcesOfAnotherEntities: int = Integer()
    CreditResources: int = Integer()
    OwnResources: int = Integer()
    LastUpdate: str = Text()
    DateStartLiquidation: str | None = Text(nullable=True)
    DateEndLiquidation: str | None = Text(nullable=True)
    CodeProvider: str = Text()
    ObjectContract: str | None = Text(nullable=True)

    class Meta:
        tablename = 'Contracts'