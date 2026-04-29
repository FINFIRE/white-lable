from django.shortcuts import render,HttpResponse,redirect
from django.utils.safestring import mark_safe
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,EQuestions14,DocumentsPrepared
from iquestions.models import IQuestions1,IQuestions2
from registration.models import User,UserDetail,UserDetail2
from connections.models import Match_Data
from datetime import datetime
from django.contrib.auth.decorators import login_required
from ..models import Capital_Matches,Matches_Purchased,Letter_Response,Purchases

def publicsecuritiesotcoverthecounter(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Public Securities</b></u><br>
    Capital Type: OTC Over the Counter</center></p>
    <p><b><u>Introduction</u></b><br>
    Over-the-Counter (OTC) securities are publicly traded financial instruments that are bought and sold directly between parties rather than through a centralized stock exchange. {n} fits that definition. OTC markets operate through dealer networks instead of formal exchanges, providing trading access for securities that may not meet listing requirements of major exchanges. In the United States, OTC markets are regulated under federal securities laws and supervised by the U.S. Securities and Exchange Commission, with trading platforms such as OTC Markets Group facilitating quotation and transparency.
    </p>
    <p><b><u>Definition of Capital Type</u></b><br>
    1. OTC markets allow securities such as stocks, bonds, derivatives, and other financial instruments to trade through broker-dealer networks instead of centralized exchanges. Companies trading OTC are often smaller, foreign, or early-stage firms that do not qualify for listing on exchanges like New York Stock Exchange or NASDAQ. Prices are negotiated directly between buyers and sellers, and dealers provide bid-ask quotations.<br>
    <br>
    2. OTC trading is best suited for small-cap companies, emerging growth firms, foreign issuers seeking U.S. investor access, and companies unable to meet stringent exchange listing standards. It offers lower regulatory costs compared to exchange listings but provides less visibility and liquidity. Investors in OTC securities are typically speculative traders, institutional investors, and retail investors seeking higher-risk opportunities.<br>
    <br>
    3. OTC securities are regulated under the Securities Exchange Act of 1934, which governs secondary market trading. Broker-dealers participating in OTC markets must be registered with the Financial Industry Regulatory Authority (FINRA). OTC Markets Group categorizes securities into tiers such as OTCQX, OTCQB, and Pink Markets based on reporting standards and disclosure levels.<br>
    <br>
    4. OTC securities generally carry higher risk due to lower liquidity, wider bid-ask spreads, and reduced regulatory oversight compared to exchange-listed securities. Companies may have limited financial disclosures, increasing information asymmetry. Market manipulation risks and price volatility are also more prevalent in certain OTC tiers.<br>
    <br>
    5. Companies seeking OTC quotation must work with a registered broker-dealer to initiate the quotation process. Financial disclosures, compliance documentation, and regulatory filings are typically required depending on the reporting status of the company. Success in OTC markets depends on transparency, investor communication, and maintaining adequate liquidity support from market makers.
    </p>
    <p><u><b>Legal Qualification Requirements</u></b><br>
    · Compliance with the Securities Exchange Act of 1934<br>
    · Broker-Dealer Sponsorship<br>
    · FINRA Registration for Market Participants<br>
    · Public Disclosure Documentation<br>
    · Ongoing Reporting Obligations (if SEC reporting company)<br>
    · AML/KYC Compliance
    </p>
    <p><u><b>Supporting Document List</u></b><br>
    · Broker-Dealer Agreement<br>
    · Company Financial Statements<br>
    · SEC Filings (if applicable)<br>
    · Corporate Governance Documents<br>
    · Market Maker Application<br>
    · Risk Disclosure Statement<br>
    · Form 211 Filing (submitted to FINRA)
    </p>
    <p><u><b>References</b></u><br>
    1. U.S. Securities and Exchange Commission. (2023). Over-the-Counter Markets Overview. https://www.sec.gov<br>
    2. OTC Markets Group. (n.d.). OTC Market Structure. https://www.otcmarkets.com<br>
    3. Securities Exchange Act of 1934. https://www.sec.gov/about/laws/sea34.pdf<br>
    4. Financial Industry Regulatory Authority. (n.d.). OTC Trading Rules. https://www.finra.org<br>
    5. Investopedia. (n.d.). Over-the-Counter (OTC) Definition. https://www.investopedia.com/terms/o/otc.asp
    </p>
    """)
    introduction = mark_safe(introduction.format(n=name))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesotcoverthecounterfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Public Securities<br>
    OTC Over the Counter</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>
    <p><u><b>1. What is OTC (Over-the-Counter) trading?</u></b><br>
    • Answer: OTC trading refers to the buying and selling of securities directly between parties through a decentralized dealer network rather than on a formal stock exchange.
    </p>
    <p><u><b>2. How does OTC trading differ from exchange trading?</u></b><br>
    • Answer: Unlike exchange trading, OTC transactions occur through broker-dealer networks without a centralized physical marketplace.
    </p>
    <p><u><b>3. What types of securities are traded OTC?</u></b><br>
    • Answer: Securities commonly traded OTC include small-cap stocks, foreign equities, bonds, derivatives, and certain digital assets.
    </p>
    <p><u><b>4. Who regulates OTC markets in the United States?</u></b><br>
    • Answer: OTC markets are regulated by authorities such as the U.S. Securities and Exchange Commission and supervised by self-regulatory organizations like Financial Industry Regulatory Authority.
    </p>
    <p><u><b>5. What is the OTC Markets Group?</u></b><br>
    • Answer: OTC Markets Group operates electronic quotation systems where broker-dealers publish bid and ask prices for OTC securities.
    </p>
    <p><u><b>6. What are the tiers within OTC markets?</u></b><br>
    • Answer: OTC markets are categorized into tiers such as OTCQX (highest standard), OTCQB (venture market), and Pink Sheets (limited reporting).
    </p>
    <p><u><b>7. Why do companies trade OTC instead of major exchanges?</u></b><br>
    • Answer: Companies may trade OTC due to lower listing requirements, reduced compliance costs, or inability to meet major exchange standards.
    </p>
    <p><u><b>8. Are OTC securities riskier than exchange-listed securities?</u></b><br>
    • Answer: OTC securities may carry higher risk due to lower liquidity, limited disclosure requirements, and greater price volatility.
    </p>
    <p><u><b>9. What role do broker-dealers play in OTC trading?</u></b><br>
    • Answer: Broker-dealers act as market makers by quoting prices and facilitating transactions between buyers and sellers.
    </p>
    <p><u><b>10. How is pricing determined in OTC markets?</u></b><br>
    • Answer: Pricing is determined through dealer quotations, supply and demand, and negotiated agreements between parties.
    </p>
    <p><u><b>11. Are OTC transactions transparent?</u></b><br>
    • Answer: OTC markets generally have less transparency compared to centralized exchanges, though reporting requirements vary by tier.
    </p>
    <p><u><b>12. Can large corporations trade OTC?</u></b><br>
    • Answer: Yes, large corporations may trade OTC for certain securities such as bonds or foreign shares not listed on U.S. exchanges.
    </p>
    <p><u><b>13. What are the advantages of OTC trading?</u></b><br>
    • Answer: Advantages include flexibility, lower listing costs, and access to niche or emerging companies.
    </p>
    <p><u><b>14. What are the disadvantages of OTC trading?</u></b><br>
    • Answer: Disadvantages include lower liquidity, higher bid-ask spreads, and increased counterparty risk.
    </p>
    <p><u><b>15. When should investors consider OTC securities?</u></b><br>
    • Answer: Investors may consider OTC securities when seeking speculative opportunities or diversification beyond major exchange-listed stocks.
    </p>
    """)
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)

def publicsecuritiesotcoverthecountertwelve(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    entity = EQuestions2.objects.get(user=request.user).Selected_Option
    stage = EQuestions1.objects.get(user=request.user).Selected_Option
    preraise = EQuestions3.objects.get(user=request.user).Selected_Option
    premarket = EQuestions4.objects.get(user=request.user).Selected_Options
    raisegoal = EQuestions5.objects.get(user=request.user).Selected_Option
    useoffund = EQuestions7.objects.get(user=request.user).Selected_Options
    enterprisecost = EQuestions8.objects.get(user=request.user).Selected_Option2
    tranch = EQuestions6.objects.get(user=request.user).Selected_Option
    rounds = EQuestions6.objects.get(user=request.user).Selected_Options
    upfrontcost = EQuestions.objects.get(user=request.user).Selected_Option
    upfronttime = EQuestions.objects.get(user=request.user).Selected_Option2
    introduction = """
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Public Securities</b></u><br>
    Capital Type: OTC Over the Counter</p></center>
    <p><b><u>1 - Stage of Development Assessment</u></b><br>
    OTC markets are typically suited for:<br>
    · Early public-stage companies<br>
    · Micro-cap and small-cap issuers<br>
    · International companies not listed on major exchanges<br>
    · Companies transitioning toward uplisting<br>
    OTC markets are often used by companies not yet meeting listing standards of major exchanges.
    </p>
    <p><b><u>2 - Entity Type Assessment</u></b><br>
    Applicable to:<br>
    · Public reporting companies<br>
    · Alternative reporting companies<br>
    · Foreign issuers<br>
    · Shell or development-stage entities<br>
    Most OTC-traded securities are C-Corporations.
    </p>
    <p><b><u>3 - Pre-Capital Assessment</u></b><br>
    Before trading OTC, companies generally require:<br>
    · Registered shares<br>
    · Transfer agent support<br>
    · Broker-dealer sponsorship<br>
    · Compliance with disclosure standards<br>
    OTC issuers may be SEC-reporting or follow alternative disclosure frameworks depending on tier.
    </p>
    <p><b><u>4 - Pre-Capital Market Type Assessment</u></b><br>
    OTC securities trade through decentralized dealer networks rather than centralized exchanges.
    Trading occurs on platforms such as OTC Markets Group, which operates tiers including OTCQX, OTCQB, and Pink Markets.
    Regulatory oversight is provided by the U.S. Securities and Exchange Commission and supervised by Financial Industry Regulatory Authority (FINRA).
    </p>
    <p><b><u>5 - Planned Total Capital to Raise Assessment</u></b><br>
    OTC trading itself does not directly raise capital.
    However, OTC-listed companies may conduct:<br>
    · Secondary offerings<br>
    · Private placements<br>
    · PIPE transactions<br>
    · Regulation A offerings<br>
    Raise sizes vary widely, typically $1 million to $50+ million for micro-cap issuers.
    </p>
    <p><b><u>6 - Capital Round Assessment</u></b><br>
    OTC trading supports secondary market liquidity, not primary issuance.
    Capital rounds occur separately through private or public offerings.
    </p>
    <p><b><u>7 - Tranche Schedule Assessment</u></b><br>
    No tranche schedule exists for OTC trading itself.
    Capital raises conducted while OTC-listed may close in:<br>
    · Single offerings<br>
    · Multiple subscription tranches<br>
    · Continuous offerings
    </p>
    <p><b><u>8 - Use of Funds Assessment</u></b><br>
    When capital is raised while OTC-listed, uses may include:<br>
    · Working capital<br>
    · Expansion<br>
    · Product development<br>
    · Debt restructuring<br>
    Use of funds must be disclosed in offering documents.
    </p>
    <p><b><u>9 - Risk Assessment</u></b><br>
    Risk level: High<br>
    Risks include:<br>
    · Lower liquidity<br>
    · Wider bid-ask spreads<br>
    · Increased volatility<br>
    · Limited analyst coverage<br>
    · Greater susceptibility to speculative trading<br>
    Investor due diligence is critical in OTC markets.
    </p>
    <p><b><u>10 - Capital Cost Assessment</u></b><br>
    Costs associated with OTC status may include:<br>
    · Market maker engagement fees<br>
    · Legal and reporting costs<br>
    · Investor relations expenses<br>
    · Potential higher discounting in capital raises<br>
    Cost of capital is often higher than major exchange-listed companies.
    </p>
    <p><b><u>11 - Up Front Cost Assessment</u></b><br>
    Upfront costs are lower than major exchange IPOs, including:<br>
    · Legal structuring<br>
    · OTC application fees<br>
    · Transfer agent and compliance setup<br>
    · Market maker sponsorship<br>
    Much less expensive than NYSE or Nasdaq listing.
    </p>
    <p><b><u>12 - Timing to Capital Assessment</u></b><br>
    OTC quotation can often be obtained within weeks to a few months, depending on compliance readiness and documentation.
    Capital raises conducted while OTC-listed may close relatively quickly if investor demand exists.
    </p>
    """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {'introduction':introduction,}
    return render(request,'detail.html',context)
