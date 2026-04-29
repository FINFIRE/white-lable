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

def bondsforeign(request):
    name = EQuestions2.objects.get(user=request.user).Business_Name
    introduction = mark_safe("""
    <p><center><b><u>Definition of Capital Market: Bonds</b></u><br>
    Capital Type: Foreign </center></p>
    <p><b><u>Introduction</u></b><br>
Foreign Bonds are ideal for investors seeking fixed-income exposure to issuers outside their domestic market, often to diversify currency, geographic, and sovereign risk. They are designed so that debt is issued by a foreign government, corporation, or supranational entity in a host country's capital market and denominated in the host country's currency. {n} fits that definition. In 2026, foreign bonds remain an important segment of international capital markets, enabling cross-border capital flows and global portfolio diversification. Common examples include Yankee bonds (foreign issuers in the U.S.), Samurai bonds (foreign issuers in Japan), and Bulldog bonds (foreign issuers in the U.K.). These instruments allow issuers to access deep local investor bases while complying with host-market regulations. While foreign bonds provide diversification and yield opportunities, they introduce currency, regulatory, and geopolitical risk. Changes in exchange rates, host-country regulations, or international relations can materially affect returns and liquidity.
    </p>

    <p><b><u>Definition of Capital Type</b></u><br>
    <br>1.A Foreign Bond is a debt security issued by a non-domestic issuer in a local capital market and denominated in the local currency of the country where the bond is issued. The bond is subject to the regulations and market practices of the host country. (International Monetary Fund, 2025)
<br>


    <br>2.  Foreign bonds occupy a position within the issuer's Capital Stack equivalent to other senior unsecured or secured debt instruments, ranking ahead of equity and subordinated capital. Investor recovery depends on issuer credit quality and governing law. (World Bank, 2025)
<br>

    <br>3. Legally, foreign bonds are governed by the securities laws, disclosure standards, and listing requirements of the host country. Issuance is typically documented through a prospectus or offering circular and distributed via local underwriting syndicates. (U.S. Securities and Exchange Commission, 2025)
<br>
    <br>4.From a risk perspective, foreign bonds expose investors to currency exchange risk, cross-border legal risk, and political risk. Even when issuer credit quality remains stable, adverse currency movements can significantly impact realized returns. (Bank for International Settlements, 2025)
<br>
    <br>5.
From an accounting and process standpoint, foreign bonds are recorded as Debt Securities by issuers and as Foreign Fixed-Income Investments by investors. Settlement, custody, and taxation depend on local market infrastructure and bilateral tax treaties. (Deloitte, 2025)
    </p>

    <p><u><b>References</u></b><br>
    <br>International Monetary Fund (IMF). (2025). International Bond Markets and Capital Flows. <a href="https://www.imf.org">https://www.imf.org</a>
<br>
    <br>World Bank. (2025). Cross-Border Debt Issuance Frameworks. <a href="https://www.worldbank.org">https://www.worldbank.org</a>
<br>
    <br>U.S. Securities and Exchange Commission (SEC). (2025). Foreign Issuers in U.S. Markets. <a href="https://www.sec.gov">https://www.sec.gov</a>
<br>
    <br>Bank for International Settlements (BIS). (2025). Global Debt Securities Statistics. <a href="https://www.bis.org">https://www.bis.org</a>
<br>
    <br>Deloitte. (2025). Accounting for Foreign Currency Debt. <a href="https://www2.deloitte.com/foreign-debt">https://www2.deloitte.com/foreign-debt</a>
<br>

    </p>

    <p><u><b>Legal Qualification Requirements</u></b>
<br>•   Issuer Status - Non-domestic government, corporate, or supranational issuer
<br>•   Host Market Compliance - Local securities laws and listing rules
<br>•   Offering Documentation - Prospectus or offering circular
<br>•   Currency Denomination - Host-country currency
<br>•   Regulatory Filings - Securities authority approvals
<br>•   Tax Withholding Rules - Local and treaty-based tax treatment
<br>•   Settlement & Custody - Local clearing systems
<br>•   Disclosure & Reporting - Ongoing issuer obligations


    </p>

    <p><b><u>Supporting Document List</u></b>
<br>•   Offering Circular / Prospectus - Bond terms and disclosures
<br>•   Underwriting Agreement - Distribution and pricing terms
<br>•   Regulatory Filings - Host-country approvals
<br>•   Currency Hedging Agreements (if applicable) - FX risk management
<br>•   Legal Opinions - Cross-border enforceability
<br>•   Tax Opinions - Withholding and treaty treatment
<br>•   Clearing & Settlement Instructions - Custody mechanics
<br>•   Credit Rating Reports - Issuer risk assessment

    </p>
        """)
    introduction = mark_safe(introduction.format(n=name))


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsforeignfaq(request):
    introduction = mark_safe("""
    <p><b><center>Capital Market: Bonds<br>
    Foreign</center></b></p>
    <p><center><u><b>Frequently Asked Question</u></b></center></p>

    <p><u><b>1. What are foreign bonds?</u></b><br>
    •Answer: Foreign bonds are debt securities issued in a domestic market by a foreign government or corporation and denominated in the local currency of that market.
</p>

    <p><u><b>2. Who issues foreign bonds?</u></b><br>
    •Answer: They are issued by foreign governments, multinational corporations, or international institutions raising capital outside their home country.
</p>

    <p><u><b>3. When are foreign bonds typically used?</u></b><br>
    •Answer: Issuers use foreign bonds to access international investors, diversify funding sources, and take advantage of favorable market conditions.
</p>

    <p><u><b>4. How do foreign bonds work?</u></b><br>
    •Answer: Investors lend money to a foreign issuer in exchange for periodic interest payments and repayment of principal at maturity.
</p>

    <p><u><b>5. How are foreign bonds different from domestic bonds?</u></b><br>
    •Answer: Foreign bonds are issued by non-domestic entities, while domestic bonds are issued by entities within the investor's country.
</p>

    <p><u><b>6. What currencies are foreign bonds issued in?</u></b><br>
    •Answer: They are typically issued in the currency of the country where the bond is sold.
</p>

    <p><u><b>7. Do foreign bonds pay regular interest?</u></b><br>
    •Answer: Yes, they generally pay fixed or floating coupon interest at regular intervals.
</p>

    <p><u><b>8. What risks are associated with foreign bonds?</u></b><br>
    •Answer: Risks include currency risk, political risk, economic instability, and issuer credit risk.
</p>

    <p><u><b>9. Are foreign bonds considered higher risk than domestic bonds?</u></b><br>
    •Answer: Often yes, due to additional country, currency, and regulatory risks.
</p>

    <p><u><b>10. Can foreign bonds be traded in secondary markets?</u></b><br>
    •Answer: Yes, many foreign bonds are tradable in international or local secondary markets.
</p>

    <p><u><b>11. How are foreign bonds taxed?</u></b><br>
    •Answer: Tax treatment varies by country and may include withholding taxes or foreign tax credits.
</p>

    <p><u><b>12. What are the benefits of investing in foreign bonds?</u></b><br>
    •Answer: Benefits include portfolio diversification, access to higher yields, and exposure to foreign economies.
</p>

    <p><u><b>13. How do foreign bonds differ from Eurobonds?</u></b><br>
    •Answer: Foreign bonds are issued in a local market and currency, while Eurobonds are issued internationally in a currency different from the issuer's home currency.
</p>

    <p><u><b>14. What types of investors invest in foreign bonds?</u></b><br>
    •Answer: Institutional investors, mutual funds, pension funds, and sophisticated individual investors commonly invest in foreign bonds.
</p>

    <p><u><b>15. When should investors consider foreign bonds?</u></b><br>
    •Answer: Investors should consider foreign bonds when seeking diversification and are comfortable with currency and geopolitical risks.
</p>

    """)


    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
def bondsforeigntwelve(request):
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
    <center><p><b><u>FINFIRE CAPITAL MATCH REPORT FOR: Bonds</b></u><br>
    Capital Type: Foreign</p></center>

    <p><b><u>1 - Stage of Development Assessment</b></u><br>
Foreign bond issuance is best suited for mature companies, financial institutions, or sovereign and quasi-sovereign entities with established operations and the scale required to access international capital markets. These instruments are generally not appropriate for early-stage companies, as issuers must demonstrate financial stability, operating history, and the ability to manage cross-border obligations.
    </p>

    <p><b><u>2 - Entity Type Assessment</b></u><br>
Eligible issuers typically include C-Corporations, multinational enterprises, financial institutions, government-backed entities, and special purpose vehicles structured for cross-border issuance. LLCs may qualify in certain jurisdictions, but sole proprietorships are not suitable due to regulatory, disclosure, and scale requirements.
    </p>

    <p><b><u>3 - Pre Capital Assessment</b></u><br>
Issuers of foreign bonds typically have significant prior capitalization and established balance sheets. Underwriting focuses on creditworthiness, currency exposure, country risk, and regulatory compliance rather than venture-style fundraising history.
    </p>

    <p><b><u>4 - Pre-Capital Market Type Assessment</b></u><br>
Foreign bonds operate within international fixed income markets and are issued outside the issuer's domestic market or denominated in a foreign currency. These markets include Eurobonds, Yankee bonds, Samurai bonds, and other jurisdiction-specific instruments accessed by global institutional investors.
    </p>

    <p><b><u>5 - Planned Total Capital to Raise Assessment</b></u><br>
Capital raised through foreign bond issuances typically ranges from tens of millions to several billion dollars, depending on issuer size, market conditions, currency selection, and investor demand. Issuance size is driven by strategic funding needs and global market appetite.
    </p>

    <p><b><u>6 - Capital Round Assessment</b></u><br>
Foreign bonds are not capital rounds and do not involve equity issuance. They are structured as debt securities with defined maturities, interest rates, and repayment schedules, often aligned with international financing or expansion strategies.
    </p>

    <p><b><u>7 - Tranche Schedule Assessment</b></u><br>
Issuances may be executed as a single tranche or multiple tranches across different currencies, maturities, or markets. Multi-tranche structures are common to optimize pricing and diversify investor exposure.
    </p>

    <p><b><u>8 - Use of Funds Assessment</b></u><br>
Proceeds from foreign bond issuances are typically used for international expansion, refinancing existing debt, acquisitions, infrastructure investment, or general corporate purposes. Use of funds is generally flexible but subject to disclosure requirements in offering documents.
<br>•   International expansion and acquisitions
<br>•   Refinancing existing debt
<br>•   Infrastructure investment
<br>•   General corporate purposes

</p>

    <p><b><u>9 - Risk Assessment</b></u><br>
Investor risk includes currency fluctuation, interest rate volatility, geopolitical risk, and differences in legal and regulatory frameworks. Issuers face foreign exchange risk, compliance complexity, and exposure to changes in international capital market conditions.
    </p>

    <p><b><u>10 - Capital Cost Assessment</b></u><br>
The cost of capital is influenced by currency selection, country risk premiums, and global interest rate environments. While foreign bonds may offer pricing advantages, additional hedging and compliance costs can increase the effective cost of capital.
    </p>

    <p><b><u>11 - Up Front Cost Assessment</b></u><br>
Upfront costs are high and include legal and regulatory compliance across jurisdictions, underwriting and placement fees, ratings assessments, disclosure documentation, and currency hedging setup. These costs are justified by access to deep global capital pools.
    </p>

    <p><b><u>12 - Timing to Capital Assessment</b></u><br>
Timing to capital is longer than domestic bond issuance due to cross-border regulatory approvals and investor marketing. The process typically ranges from several months to over a year, depending on jurisdiction and complexity.
</p>
        """
    introduction = mark_safe(introduction.format(rounds=rounds,entity=entity,stage=stage,n=name,preraise=preraise,premarket=premarket,raisegoal=raisegoal,useoffund=useoffund,enterprisecost=enterprisecost,tranch=tranch,upfrontcost=upfrontcost,upfronttime=upfronttime))
    context = {
        'introduction':introduction,
    }
    return render(request,'detail.html',context)
