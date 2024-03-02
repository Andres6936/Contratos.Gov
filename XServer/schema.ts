import {integer, real, sqliteTable, text} from "drizzle-orm/sqlite-core";

export const contracts = sqliteTable('Contracts', {
    Serial: text('Serial').primaryKey(),
    NameEntity: text('NameEntity'),
    NitEntity: integer('NitEntity'),
    EntityCode: integer('EntityCode'),
    Department: text('Department'),
    City: text('City'),
    Location: text('Location'),
    Order: text('Order'),
    Sector: text('Sector'),
    Branch: text('Branch'),
    CentralEntity: text('CentralEntity'),
    ProcessPurchase: text('ProcessPurchase'),
    SerialContract: text('SerialContract'),
    ReferenceContract: text('ReferenceContract'),
    StateContract: text('StateContract'),
    CodeCategoryMain: text('CodeCategoryMain'),
    DescriptionProcess: text('DescriptionProcess'),
    TypeContract: text('TypeContract'),
    ContractingMode: text('ContractingMode'),
    JustifyContractingMode: text('JustifyContractingMode'),
    DateSign: text('DateSign'),
    DateStartContract: text('DateStartContract'),
    DateEndContract: text('DateEndContract'),
    DateStartExecution: text('DateStartExecution'),
    DateEndExecution: text('DateEndExecution'),
    DeliveryConditions: text('DeliveryConditions'),
    ProviderTypeDocument: text('ProviderTypeDocument'),
    ProviderDocument: text('ProviderDocument'),
    ProviderAwarder: text('ProviderAwarder'),
    IsGroup: text('IsGroup'),
    IsPyme: text('IsPyme'),
    EnableAdvancePayment: text('EnableAdvancePayment'),
    Liquidation: text('Liquidation'),
    EnvironmentalObligation: text('EnvironmentalObligation'),
    PostConsumerObligation: text('PostConsumerObligation'),
    Reversal: text('Reversal'),
    ValueContract: integer('ValueContract'),
    ValueEnableAdvancePayment: integer('ValueEnableAdvancePayment'),
    ValueInvoice: integer('ValueInvoice'),
    ValuePendingPayment: integer('ValuePendingPayment'),
    ValuePaid: integer('ValuePaid'),
    ValueAmortized: integer('ValueAmortized'),
    ValuePendingAmortized: integer('ValuePendingAmortized'),
    ValuePendingExecution: integer('ValuePendingExecution'),
    StateBankOfNationalInvestmentProjects: text('StateBankOfNationalInvestmentProjects'),
    CodeBankOfNationalInvestmentProjects: text('CodeBankOfNationalInvestmentProjects'),
    YearBankOfNationalInvestmentProjects: text('YearBankOfNationalInvestmentProjects'),
    BalanceCertificateOfBudgetaryAvailability: real('BalanceCertificateOfBudgetaryAvailability'),
    BalanceVigence: integer('BalanceVigence'),
    IsPostConflict: text('IsPostConflict'),
    ProcessUrl: text('ProcessUrl'),
    ExpenseDestination: text('ExpenseDestination'),
    OrigenResources: text('OrigenResources'),
    DaysAdded: integer('DaysAdded'),
    PointsOfTheAgreement: text('PointsOfTheAgreement'),
    PillarsOfTheAgreement: text('PillarsOfTheAgreement'),
    LegalRepresentativeName: text('LegalRepresentativeName'),
    LegalRepresentativeNationality: text('LegalRepresentativeNationality'),
    LegalRepresentativeTypeIdentification: text('LegalRepresentativeTypeIdentification'),
    LegalRepresentativeGender: text('LegalRepresentativeGender'),
    GeneralBudgetOfNation: integer('GeneralBudgetOfNation'),
    GeneralParticipationSystem: integer('GeneralParticipationSystem'),
    GeneralRoyaltiesSystem: integer('GeneralRoyaltiesSystem'),
    ResourcesOfAnotherEntities: integer('ResourcesOfAnotherEntities'),
    CreditResources: integer('CreditResources'),
    OwnResources: integer('OwnResources'),
    LastUpdate: text('LastUpdate'),
    DateStartLiquidation: text('DateStartLiquidation'),
    DateEndLiquidation: text('DateEndLiquidation'),
    CodeProvider: text('CodeProvider'),
    ObjectContract: text('ObjectContract'),
});
