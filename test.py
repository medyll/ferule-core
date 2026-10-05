#!/usr/bin/env python3
"""
Ferule-Core Quick Test Suite

Run all module tests to verify everything is operational.
"""

import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_test(name, command, expected_in_output=None):
    print(f"\n{'='*70}")
    print(f"🧪 TEST: {name}")
    print(f"{'='*70}")
    print(f"Command: {command}")
    print()
    
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run(command, shell=True, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", env=env)
    
    print(result.stdout[:2000] if len(result.stdout) > 2000 else result.stdout)
    
    if result.returncode != 0:
        print(f"\n❌ FAILED: Exit code {result.returncode}")
        if result.stderr:
            print(f"Error: {result.stderr[:500]}")
        return False
    
    if expected_in_output and expected_in_output not in result.stdout:
        print(f"\n❌ FAILED: Expected '{expected_in_output}' in output")
        return False
    
    print(f"\n✅ PASSED")
    return True


def main():
    print("="*70)
    print("🔮 FERULE-CORE — Test Suite")
    print("="*70)
    
    tests_passed = 0
    tests_total = 0
    
    # Test 1: Matrix Topology - Demo
    tests_total += 1
    if run_test(
        "Matrix Topology — Demo Mode",
        f"\"{sys.executable}\" {BASE_DIR}/matrix-topology/skill/matrix-topology/scripts/encode.py --demo",
        "BIO_URGENCY"
    ):
        tests_passed += 1
    
    # Test 2: Matrix Topology - Single Text
    tests_total += 1
    if run_test(
        "Matrix Topology — Single Text",
        f"\"{sys.executable}\" {BASE_DIR}/matrix-topology/skill/matrix-topology/scripts/encode.py \"Je réfléchis à un concept abstrait\"",
        "ABSTRACT_HEURISTICS"
    ):
        tests_passed += 1
    
    # Test 3: Matrix Topology - List Constellations
    tests_total += 1
    if run_test(
        "Matrix Topology — List Constellations",
        f"\"{sys.executable}\" {BASE_DIR}/matrix-topology/skill/matrix-topology/scripts/encode.py --constellations",
        "LATENT_EXPLORATION"
    ):
        tests_passed += 1
    
    # Test 4: Structural Mapping - Demo
    tests_total += 1
    if run_test(
        "Structural Mapping — Caféine Demo",
        f"\"{sys.executable}\" {BASE_DIR}/structural-mapping/skill/structural-mapping/scripts/matrix.py --demo",
        "ind-rea-sitac"
    ):
        tests_passed += 1
    
    # Test 5: LLM Indicators - Demo
    tests_total += 1
    if run_test(
        "LLM Indicators — Demo Mode",
        f"\"{sys.executable}\" {BASE_DIR}/structural-mapping/skill/structural-mapping/scripts/llm_indicators.py --demo",
        "tech_startup"
    ):
        tests_passed += 1
    
    # Test 6: Check Dashboard exists
    tests_total += 1
    dashboard_path = f"{BASE_DIR}/dashboard.html"
    if os.path.exists(dashboard_path):
        size = os.path.getsize(dashboard_path)
        print(f"\n{'='*70}")
        print(f"🧪 TEST: Dashboard HTML")
        print(f"{'='*70}")
        print(f"Path: {dashboard_path}")
        print(f"Size: {size} bytes")
        if size > 10000:
            print(f"\n✅ PASSED")
            tests_passed += 1
        else:
            print(f"\n❌ FAILED: Dashboard too small")
    else:
        print(f"\n{'='*70}")
        print(f"🧪 TEST: Dashboard HTML")
        print(f"{'='*70}")
        print(f"\n❌ FAILED: Dashboard not found at {dashboard_path}")
    
    # Test 7: Check 3D Dashboard exists
    tests_total += 1
    dashboard_3d_path = f"{BASE_DIR}/dashboard-3d.html"
    if os.path.exists(dashboard_3d_path):
        size = os.path.getsize(dashboard_3d_path)
        print(f"\n{'='*70}")
        print(f"🧪 TEST: Dashboard 3D HTML")
        print(f"{'='*70}")
        print(f"Path: {dashboard_3d_path}")
        print(f"Size: {size} bytes")
        if size > 10000:
            print(f"\n✅ PASSED")
            tests_passed += 1
        else:
            print(f"\n❌ FAILED: Dashboard 3D too small")
    else:
        print(f"\n{'='*70}")
        print(f"🧪 TEST: Dashboard 3D HTML")
        print(f"{'='*70}")
        print(f"\n❌ FAILED: Dashboard 3D not found at {dashboard_3d_path}")
    
    # Summary
    print(f"\n{'='*70}")
    print(f"📊 TEST SUMMARY")
    print(f"{'='*70}")
    print(f"Passed: {tests_passed}/{tests_total}")
    print(f"Success Rate: {(tests_passed/tests_total)*100:.1f}%")
    
    if tests_passed == tests_total:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"\n📍 Next steps:")
        print(f"   1. Open dashboard.html (2D interface)")
        print(f"   2. Open dashboard-3d.html (3D visualization with Three.js)")
        print(f"   3. Test LLM indicator generation")
        return 0
    else:
        print(f"\n⚠️  Some tests failed. Check output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
