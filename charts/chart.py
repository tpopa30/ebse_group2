# This script was written with assistance from GPT 5 Chat. The first chart was made by hand and the following were 
# generated based on that to fit new data.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

TITLE_FONT_SIZE = 18
LABEL_FONT_SIZE = 16
FONT_SIZE = 14

sns.set(style="whitegrid")

# Make directories rq1, rq2, rq3, general if they don't exist
import os
os.makedirs("rq1", exist_ok=True)
os.makedirs("rq2", exist_ok=True)
os.makedirs("rq3", exist_ok=True)
os.makedirs("general", exist_ok=True)

# Papers Answering Each Research Question
rq_data = pd.DataFrame({
    "Research Question": ["RQ1", "RQ2", "RQ3"],
    "Papers Answering It": [17, 13, 9]
})

plt.figure(figsize=(10, 7))
ax4 = sns.barplot(
    data=rq_data,
    x="Research Question",
    y="Papers Answering It",
    palette="flare",
    width=0.5
)

for p in ax4.patches:
    height = p.get_height()
    ax4.annotate(f'{int(height)}',
                 (p.get_x() + p.get_width() / 2., height),
                 ha='center', va='bottom',
                 fontsize=FONT_SIZE,
                 xytext=(0, 3),
                 textcoords='offset points')

plt.title("Number of Papers Answering Each Research Question", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Research Question", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.yticks(fontsize=FONT_SIZE)

plt.tight_layout(pad=3.0)
plt.savefig("general/chart_research_questions.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: general/chart_research_questions.png")

# Quality Assessment Score Distribution
score_data = pd.DataFrame({
    "Score": [1, 1.5, 1.75, 2],
    "Count": [0, 6, 3, 14]
})

plt.figure(figsize=(10, 7))
ax5 = sns.barplot(
    data=score_data,
    x="Score",
    y="Count",
    palette="Blues",
    width=0.5
)

for p in ax5.patches:
    height = p.get_height()
    ax5.annotate(f'{int(height)}',
                 (p.get_x() + p.get_width() / 2., height),
                 ha='center', va='bottom',
                 fontsize=FONT_SIZE,
                 xytext=(0, 3),
                 textcoords='offset points')

plt.title("Quality Assessment Score Distribution", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Score", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.ylabel("Count", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.yticks(fontsize=FONT_SIZE)
plt.ylim(0, max(score_data["Count"]) + 2)

plt.tight_layout(pad=3.0)
plt.savefig("general/chart_quality_assessment_scores.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: general/chart_quality_assessment_scores.png")

# Loading RQ3 Dataset

rq3_df = pd.read_csv("rq3_data.csv", sep=None, engine="python")
rq3_df.columns = rq3_df.columns.str.strip()
rq3_df = rq3_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
rq3_df = rq3_df.replace(["N/A", ""], pd.NA)
rq3_df = rq3_df.dropna(how='all', subset=["Optimisation Method Category", "Schedulling or Power Capping"])

# Rq3. Schedulling or Power Capping

plt.figure(figsize=(12, 8))
sched_counts = (
    rq3_df["Schedulling or Power Capping"]
      .value_counts(dropna=False)
      .reset_index()
)
sched_counts.columns = ["Schedulling or Power Capping", "Count"]

ax1 = sns.barplot(
    data=sched_counts,
    x="Schedulling or Power Capping",
    y="Count",
    palette="crest",
    width=0.5
)
ax1.bar_label(ax1.containers[0], fmt='%d', label_type='edge', padding=2, fontsize=FONT_SIZE)
plt.title("Distribution of Scheduling / Power-Capping Approaches", fontsize=TITLE_FONT_SIZE, pad=15)
plt.xlabel("Schedulling or Power Capping", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.tight_layout(pad=2.0)
plt.savefig("rq3/sched_or_powercap_distribution.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq3/sched_or_powercap_distribution.png")

# Rq3. Optimisation Method Category
plt.figure(figsize=(12, 8))
method_counts = (
    rq3_df["Optimisation Method Category"]
      .value_counts(dropna=False)
      .reset_index()
)
method_counts.columns = ["Optimisation Method Category", "Count"]

ax2 = sns.barplot(
    data=method_counts,
    x="Optimisation Method Category",
    y="Count",
    palette="mako",
    width=0.5
)
ax2.bar_label(ax2.containers[0], fmt='%d', label_type='edge', padding=2, fontsize=FONT_SIZE)
plt.title("Distribution of Optimisation Methods", fontsize=TITLE_FONT_SIZE, pad=15)
plt.xlabel("Optimisation Method Category", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.tight_layout(pad=2.0)
plt.savefig("rq3/optimisation_method_distribution.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq3/optimisation_method_distribution.png")

# Rq3. Grouped Bar Chart
counts = (
    rq3_df.groupby(["Optimisation Method Category", "Schedulling or Power Capping"])
      .size()
      .reset_index(name="Count")
)

plt.figure(figsize=(14, 9))
ax3 = sns.barplot(
    data=counts,
    x="Optimisation Method Category",
    y="Count",
    hue="Schedulling or Power Capping",
    palette="viridis",
    width=0.55,
    dodge=True
)

for container in ax3.containers:
    ax3.bar_label(container, fmt='%d', label_type='edge', padding=2, fontsize=FONT_SIZE)

plt.title("Optimisation Methods vs Scheduling / Power-Capping Approaches", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Optimisation Method Category", fontsize=LABEL_FONT_SIZE, labelpad=25)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0, ha="center")
plt.yticks(fontsize=FONT_SIZE)
plt.legend(title="Schedulling or Power Capping",
           loc="upper center",
           bbox_to_anchor=(0.5, -0.12),
           ncol=2,
           fontsize=FONT_SIZE - 2,
           title_fontsize=FONT_SIZE - 1,
           frameon=False)

plt.tight_layout(pad=3.0)
plt.savefig("rq3/optimisation_methods_vs_approaches.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq3/optimisation_methods_vs_approaches.png")


# Rq1. Overview of Combined Methods
overview_data = pd.DataFrame({
    "Methods used": ["Uses Hardware", "Uses Software", "Uses ML Model / Simulation"],
    "Total": [14, 13, 13],
    "Hybrid": [9, 10, 9],
    "Single": [5, 3, 4]
})

overview_long = overview_data.melt(
    id_vars="Methods used",
    var_name="Category",
    value_name="No. of papers"
)

plt.figure(figsize=(12, 8))
ax = sns.barplot(
    data=overview_long,
    x="Methods used",
    y="No. of papers",
    hue="Category",
    palette=["#4285F4", "#FB8C00", "#00ACC1"],
    width=0.6
)

for p in ax.patches:
    height = p.get_height()
    ax.annotate(f'{int(height)}',
                (p.get_x() + p.get_width() / 2., height),
                ha='center', va='bottom',
                fontsize=FONT_SIZE,
                xytext=(0, 3),
                textcoords='offset points')

plt.title("Overview of Combined Methods", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Methods used", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("No. of papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.yticks(fontsize=FONT_SIZE)

plt.legend(title=None, fontsize=FONT_SIZE, loc="upper right")
plt.tight_layout(pad=3.0)
plt.savefig("rq1/chart_overview_combined_methods.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq1/chart_overview_combined_methods.png")

# Rq2. Hardware Type
hw_data = pd.DataFrame({
    "Hardware Type": ["Enterprise", "Consumer", "Both", "Unknown / Not Specified"],
    "Count": [12, 5, 3, 3]
})

plt.figure(figsize=(10, 7))
ax_hw = sns.barplot(
    data=hw_data,
    x="Hardware Type",
    y="Count",
    palette="crest",
    width=0.6
)

for p in ax_hw.patches:
    height = p.get_height()
    ax_hw.annotate(f'{int(height)}', 
                   (p.get_x() + p.get_width()/2., height), 
                   ha='center', va='bottom', 
                   fontsize=FONT_SIZE, xytext=(0, 3),
                   textcoords='offset points')

plt.title("Distribution of Hardware Types", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Hardware Type", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.yticks(fontsize=FONT_SIZE)
plt.tight_layout(pad=3.0)
plt.savefig("rq2/chart_hw_type.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq2/chart_hw_type.png")


# RQ2. CPU Vendor
cpu_data = pd.DataFrame({
    "CPU Vendor": ["Intel", "AMD", "ARM", "Unknown / Not Specified"],
    "Count": [17, 2, 3, 3]
})

plt.figure(figsize=(10, 7))
ax_cpu = sns.barplot(
    data=cpu_data,
    x="CPU Vendor",
    y="Count",
    palette="mako",
    width=0.6
)

for p in ax_cpu.patches:
    height = p.get_height()
    ax_cpu.annotate(f'{int(height)}',
                    (p.get_x() + p.get_width()/2., height),
                    ha='center', va='bottom',
                    fontsize=FONT_SIZE, xytext=(0, 3),
                    textcoords='offset points')

plt.title("Distribution of CPU Vendors", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("CPU Vendor", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.yticks(fontsize=FONT_SIZE)
plt.tight_layout(pad=3.0)
plt.savefig("rq2/chart_cpu_vendor.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq2/chart_cpu_vendor.png")


# Rq2. Containerisation Platform
platform_data = pd.DataFrame({
    "Containerisation Platform": ["Kubernetes", "Docker", "Both", "Both + Other", "Other"],
    "Count": [12, 3, 3, 1, 4]
})

plt.figure(figsize=(10, 7))
ax_platform = sns.barplot(
    data=platform_data,
    x="Containerisation Platform",
    y="Count",
    palette="flare",
    width=0.6
)

for p in ax_platform.patches:
    height = p.get_height()
    ax_platform.annotate(f'{int(height)}',
                         (p.get_x() + p.get_width()/2., height),
                         ha='center', va='bottom',
                         fontsize=FONT_SIZE, xytext=(0, 3),
                         textcoords='offset points')

plt.title("Containerisation Platforms Used", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Containerisation Platform", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=15, ha="right")
plt.yticks(fontsize=FONT_SIZE)
plt.tight_layout(pad=3.0)
plt.savefig("rq2/chart_containerisation_platforms.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq2/chart_containerisation_platforms.png")

# Rq1. Hardware Measurement Methods
hardware_measure_data = pd.DataFrame({
    "Measurement Method": [
        "Intel RAPL",
        "External Power Meter",
        "PMC",
        "HWPC"
    ],
    "Count": [13, 6, 5, 1]
})

plt.figure(figsize=(10, 7))
ax_hw_measure = sns.barplot(
    data=hardware_measure_data,
    x="Measurement Method",
    y="Count",
    palette="crest",
    width=0.6
)

for p in ax_hw_measure.patches:
    height = p.get_height()
    ax_hw_measure.annotate(
        f'{int(height)}',
        (p.get_x() + p.get_width() / 2.0, height),
        ha='center',
        va='bottom',
        fontsize=FONT_SIZE,
        xytext=(0, 3),
        textcoords='offset points'
    )

plt.title("Distribution of Hardware Measurement Methods",
          fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Measurement Method", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=20, ha="right")
plt.yticks(fontsize=FONT_SIZE)
plt.tight_layout(pad=3.0)
plt.savefig("rq1/chart_hw_measurement_methods.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq1/chart_hw_measurement_methods.png")

software_measure_data = {
    "Kepler": 7,
    "Scaphandre": 3,
    "Prometheus": 3,
    "Berkley Packet Filter": 3,
    "KubeWatt": 1,
    "SmartWatts": 1,
    "Containergy": 1,
    "WattsApp": 1
}

# ORder the data by the number from highest to lowest
software_measure_data = dict(sorted(software_measure_data.items(), key=lambda item: item[1], reverse=True))

software_measure_data = pd.DataFrame({
    "Measurement Method": list(software_measure_data.keys()),
    "Count": list(software_measure_data.values())
})

plt.figure(figsize=(12, 7))
ax_sw_measure = sns.barplot(
    data=software_measure_data,
    x="Measurement Method",
    y="Count",
    palette="mako",
    width=0.6
)

for p in ax_sw_measure.patches:
    height = p.get_height()
    ax_sw_measure.annotate(
        f'{int(height)}',
        (p.get_x() + p.get_width() / 2.0, height),
        ha='center',
        va='bottom',
        fontsize=FONT_SIZE,
        xytext=(0, 3),
        textcoords='offset points'
    )

plt.title("Distribution of Software Measurement Methods", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Measurement Method", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=30, ha="right")
plt.yticks(fontsize=FONT_SIZE)
plt.tight_layout(pad=3.0)
plt.savefig("rq1/chart_software_measurement_methods.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq1/chart_software_measurement_methods.png")

# Rq1. Research Approaches
approach_data = pd.DataFrame({
    "Approach Type": ["Machine Learning", "Analytical", "Simulation"],
    "Count": [5, 5, 4]
})

plt.figure(figsize=(10, 7))
ax_approach = sns.barplot(
    data=approach_data,
    x="Approach Type",
    y="Count",
    palette="rocket",
    width=0.6
)

for p in ax_approach.patches:
    height = p.get_height()
    ax_approach.annotate(
        f'{int(height)}',
        (p.get_x() + p.get_width() / 2.0, height),
        ha='center',
        va='bottom',
        fontsize=FONT_SIZE,
        xytext=(0, 3),
        textcoords='offset points'
    )

plt.title("Approaches for Measuring Container Energy Usage", fontsize=TITLE_FONT_SIZE, pad=25)
plt.xlabel("Approach Type", fontsize=LABEL_FONT_SIZE, labelpad=20)
plt.ylabel("Number of Papers", fontsize=LABEL_FONT_SIZE, labelpad=15)
plt.xticks(fontsize=FONT_SIZE, rotation=0)
plt.yticks(fontsize=FONT_SIZE)
plt.tight_layout(pad=3.0)
plt.savefig("rq1/chart_research_approaches.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved: rq1/chart_research_approaches.png")